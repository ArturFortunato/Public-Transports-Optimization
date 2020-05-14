import pandas as pd


#Create datasets for estimating number of people entering a station at a given time


file = "parsed_data/full_data/samplemetro_only_entries_station_names.csv"
endfolder1 = "parsed_data/data_per_station_count/"
endfolder2 = "parsed_data/data_per_station_exits/"

stations =['aeroporto', 'alameda', 'alfornelos', 'alto dos moinhos', 'alvalade', 'amadora este', 'ameixoeira', 'anjos', 'areeiro', 'avenida', 'baixa chiado', 'bela vista', 'cabo ruivo', 'cais do sodré', 'campo grande', 'campo pequeno', 'carnide', 'chelas', 'cidade universitária', 'colégio militar', 'encarnação', 'entre campos', 'intendente', 'jardim zoológico', 'laranjeiras', 'lumiar', 'marquês de pombal', 'martim moniz', 'moscavide', 'odivelas', 'olaias', 'olivais', 'oriente', 'parque', 'picoas', 'pontinha', 'praça de espanha', 'quinta das conchas', 'rato', 'reboleira', 'restauradores', 'roma', 'rossio', 'saldanha', 'santa apolónia', 'são sebastião', 'senhor roubado', 'telheiras', 'terreiro paço']


def generate_count_per_station_per_hour():
    csv = pd.read_csv(file, encoding = "ISO-8859-1", sep=',', header=0, skipinitialspace=True)
    
    del csv['id']
    del csv['linha_entrada']
    del csv['linha_saida']
    del csv['estacao_saida']
    
        
    
    for station in stations:
        reduced = csv[csv['estacao_entrada'] == station]
        summed = reduced.groupby('date')['count'].sum()
        summed.to_csv(endfolder1 + station + ".csv", index=True, sep=',')    
        
    return "done"


def generate_exits_per_station_per_hour():
    csv = pd.read_csv(file, encoding = "ISO-8859-1", sep=',', header=0, skipinitialspace=True)
    
    del csv['id']
    del csv['linha_entrada']
    del csv['linha_saida']
    
    csv['date'] = csv['date'].str[11:]
    
    for station in stations:
        reduced = csv[csv['estacao_entrada'] == station]
        summed = reduced.groupby(['date', 'estacao_saida'])['count'].sum()
        summed.to_csv(endfolder2 + station + ".csv", index=True, sep=',')    
        
    return "done"

#generate_count_per_station_per_hour()
#generate_exits_per_station_per_hour()
