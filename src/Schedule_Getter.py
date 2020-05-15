from pandas_ods_reader import read_ods

entry_lines = {}
entry_lines["entradas"] = {}
entry_lines["saidas"] = {}

for cor in ["blue","yellow","green","red"]:
    for tipo in ["entradas","saidas"]:
        path = "schedules/linha_" + cor + "_" + tipo + "1.ods"
        sheet_idx = 1
        df = read_ods(path, sheet_idx)
        entry_lines[tipo][cor] = df
        #print("cor " + str(cor) + str(df.shape))

#path = "linha_vermelha_entradas1.ods"
#sheet_idx = 1
#df4 = read_ods(path, sheet_idx)


hours_dicio = {}
#criacao de um dicionario com as horas
with open('horas.txt') as openfileobject:
    counter = 0
    for line in openfileobject:
        line = line.replace(" ","").replace("\n","")
        hours_dicio[line] = counter
        counter += 1


#tipo e um booleano que devolve entradas e saidas
def extract_value(line,hour,station,tipo):

    line = entry_lines[tipo][line]
    index = hours_dicio[hour]
    res = line[station][index]


    res = str(res)

    try:
        float(res)
        if(res == "nan"):
            return 0
        return float(res)
    except ValueError:
        return 0        
    

print(entry_lines["saidas"]["yellow"].keys())
print(extract_value("yellow",'07:45-60',"Rato","saidas"))