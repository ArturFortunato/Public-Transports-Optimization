# - coding: utf-8 --
import pandas as pd

from global_vars import stations
#Create datasets for estimating number of people entering d station at d given time

file = "parsed_data/full_data/samplemetro_only_entries_station_names.csv"
endfolder1 = "parsed_data/data_per_station_count/"
endfolder2 = "parsed_data/data_per_station_exits/"

def generate_count_per_station_per_hour():
    csv = pd.read_csv(file, sep=',', header=0, skipinitialspace=True)
    

    del csv['id']
    del csv['linha_entrada']
    del csv['linha_saida']
    del csv['estacao_saida'] 

    #hack
    add = "2018-10-01 00:00:00,0\n2018-11-01 23:45:00,0\n"
    
    for station in stations:
        reduced = csv[csv['estacao_entrada'] == station]
        summed = reduced.groupby('date')['count'].sum()
        summed.to_csv(endfolder1 + station + ".csv", index=True, sep=',', header=["count"])
        with open(endfolder1 + station + ".csv", 'a', encoding = "latin1") as f:
            f.write(add)
    return "done"

def generate_exits_per_station_per_hour():
    csv = pd.read_csv(file, sep=',', header=0, skipinitialspace=True)

    del csv['id']
    del csv['linha_entrada']
    del csv['linha_saida']
    
    csv['date'] = csv['date'].str[11:]
    
    for station in stations:
        reduced = csv[csv['estacao_entrada'] == station]
        summed = reduced.groupby(['date', 'estacao_saida'])['count'].sum()
        #print(summed)
        summed.to_csv(endfolder2 + station + ".csv", index=True, sep=',', header=["count"])    
        
    return "done"

#GERA OS EXCEIS!!! LENTO... CERTIFICAR QUE ELES EXISTEM ANTES DE CORRER
generate_count_per_station_per_hour()
generate_exits_per_station_per_hour()