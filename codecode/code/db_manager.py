'''
@info abstract class to support database operations of urban data sources
@author Rui Henriques
@version 1.0
'''

import csv, abc, time
from ilu.database import db_connection
from ilu.utils import math_utils

class DataManager():
    
    def __init__(self,tablenames,heads):
        self.db = db_connection.Database()
        self.tables = tablenames
        self.heads = heads
        
    @abc.abstractmethod    
    def transform_data(self):
        return

    def repopulate_database(self):
        success = True
        
        #A: drop and recreate tables in database
        for i in range(0,len(self.tables)):
            self.db.remove_table(self.tables[i])
            self.db.create_table(self.tables[i],self.heads[i])
    
        #B: populate table
        temp_files = self.transform_data()
        for i in range(0,len(self.tables)):
            reader = csv.reader(open(temp_files[i], 'r'), delimiter=',')
            print(self.tables[i])
            isuccess = self.db.populate_table(self.tables[i],self.heads[i],reader)
            if isuccess is False: break
            success = success and isuccess 
        return success
        
    def get_unique_values_per_column(self,columns):
        result = {}
        tablename, head = self.tables[0], self.heads[0]
        for col in columns:
            query = "SELECT DISTINCT "+col+" FROM "+tablename+" ORDER BY "+col
            df = self.db.get_table_from_query(query)
            mlist = df[col].values.tolist()
            if head[col]=='int': mlist = math_utils.to_int(mlist)
            result[col] = mlist
        return result
    
class JsonDataManager(DataManager):
    
    def __init__(self,tablenames,heads):
        DataManager.__init__(self,tablenames,heads)

    def assess_performance(self,datafile):
        for mode in ['incremental','all']:
            fp = open(datafile,'rb')
            start = time.time()
            if mode is 'all': self.all_json_parsing(fp)
            else: self.inc_json_parsing(fp)
            print('Mode:',mode,' time=',time.time()-start)

    @abc.abstractmethod    
    def inc_json_parsing(self,file,writers):
        return

    @abc.abstractmethod    
    def all_json_parsing(self,file,writers):
        return

    @abc.abstractmethod    
    def write_line(self,writer,entry,head):
        return
