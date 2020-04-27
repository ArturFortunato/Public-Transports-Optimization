'''
@info database connector for query execution
@author Rui Henriques
@version 1.0
'''

from cubes import Workspace
from itertools import zip_longest
import psycopg2, os, pandas.io.sql as psql
from ilu.database import dw_process

class Database(object):

    def __init__(self):
        
        #A: connection details
        user = 'postgres'
        password = 'root'
        host = '127.0.0.1' #localhost
        port = '5432'
        database = 'iludb'
        
        #B: database connection
        self.conn = psycopg2.connect(user=user,password=password,host=host,port=port,database=database)
        
        #C: data warehouse connection
        self.workspace = Workspace()
        dburl = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
        directory = os.path.dirname(os.path.abspath(__file__))+'/'
        self.workspace.register_default_store("sql", url=dburl)
        tempfilename = dw_process.process(directory+"ilumodel.json")
        self.workspace.import_model(tempfilename)

    def __end__(self):
        if(self.conn): self.conn.close()
    
    def get_data(self, query):
        return psql.read_sql_query(query, self.conn)
    
    def execute_query(self, query):
        success = True
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
        except Exception as error : 
            print(query)
            print('Error while executing a query to PostgreSQL', error)
            success = False
        finally: 
            if(self.conn): cursor.close()
        return success

    def remove_table(self, tablename):
        try:
            cursor = self.conn.cursor()
            cursor.execute("select exists(select * from information_schema.tables where table_name='%s')"%tablename)
            exists = cursor.fetchone()[0]
            if exists:
                success = self.execute_query('DROP TABLE '+tablename)
                if success: print('Drop query successful executed')
                return success
            else: print('Non-existing table')
        except Exception as error : 
            print('Error while executing a query to PostgreSQL', error)
        return False
        
    def create_table(self, tablename, head_dic):
        print(tablename)
        createTableQuery = 'CREATE TABLE '+tablename+' ('
        for key in head_dic: createTableQuery += key+' '+head_dic[key]+','
        success = self.execute_query(createTableQuery[:-1]+')')
        if success: print('Create query successful executed')
        return success
    
    def get_table(self, tablename, columns=None, where=None):
        cols = "*" if columns==None else "("+','.join(columns)+")"
        query = "SELECT "+cols+" FROM "+tablename
        if where is not None: query=query+" "+where
        return psql.read_sql(query, self.conn)

    def get_table_from_query(self, query):
        return psql.read_sql(query, self.conn)
    
    def get_all_tables(self):
        result = []
        cursor = self.conn.cursor()
        cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        for entry in cursor.fetchall():
            result.append(entry[0])
        return result
    
    def populate_table(self, tablename, head_dic, data_reader):
        next(data_reader)
        for next_n_lines in zip_longest(*[data_reader] * 10):
            insertTableQuery = 'INSERT INTO '+tablename+' ('+','.join(list(head_dic))+')\nVALUES\n'
            insertTableQuery = insertTableQuery.replace('(id,','(')
            for row in next_n_lines:
                if row is None : break
                values = '(\''+('\',\''.join(row))+'\'),\n'
                insertTableQuery += values.replace(',\'\'',',null').replace(';',',')
            success = self.execute_query(insertTableQuery[:-2]+';')
            if not(success): return success
        print('Populate queries executed successfully')
        return True     
