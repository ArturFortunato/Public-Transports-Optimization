# - coding: utf-8 --

import pandas as pd
import datetime
import pickle
import random
import numpy
import glob
import os

from tslearn.barycenters import softdtw_barycenter
from itertools import chain

from global_vars import stations
from global_vars import RED, GREEN, BLUE, YELLOW


#Mapping Hour to int
date_values = {'00:00:00': 0, '00:15:00': 1, '00:30:00': 2, '00:45:00': 3, '01:00:00': 4, '01:15:00': 5, '01:30:00': 6, '01:45:00': 7, '02:00:00': 8, '02:15:00': 9, '02:30:00': 10, '02:45:00': 11, '03:00:00': 12, '03:15:00': 13, '03:30:00': 14, '03:45:00': 15, '04:00:00': 16, '04:15:00': 17, '04:30:00': 18, '04:45:00': 19, '05:00:00': 20, '05:15:00': 21, '05:30:00': 22, '05:45:00': 23, '06:00:00': 24, '06:15:00': 25, '06:30:00': 26, '06:45:00': 27, '07:00:00': 28, '07:15:00': 29, '07:30:00': 30, '07:45:00': 31, '08:00:00': 32, '08:15:00': 33, '08:30:00': 34, '08:45:00': 35, '09:00:00': 36, '09:15:00': 37, '09:30:00': 38, '09:45:00': 39, '10:00:00': 40, '10:15:00': 41, '10:30:00': 42, '10:45:00': 43, '11:00:00': 44, '11:15:00': 45, '11:30:00': 46, '11:45:00': 47, '12:00:00': 48, '12:15:00': 49, '12:30:00': 50, '12:45:00': 51, '13:00:00': 52, '13:15:00': 53, '13:30:00': 54, '13:45:00': 55, '14:00:00': 56, '14:15:00': 57, '14:30:00': 58, '14:45:00': 59, '15:00:00': 60, '15:15:00': 61, '15:30:00': 62, '15:45:00': 63, '16:00:00': 64, '16:15:00': 65, '16:30:00': 66, '16:45:00': 67, '17:00:00': 68, '17:15:00': 69, '17:30:00': 70, '17:45:00': 71, '18:00:00': 72, '18:15:00': 73, '18:30:00': 74, '18:45:00': 75, '19:00:00': 76, '19:15:00': 77, '19:30:00': 78, '19:45:00': 79, '20:00:00': 80, '20:15:00': 81, '20:30:00': 82, '20:45:00': 83, '21:00:00': 84, '21:15:00': 85, '21:30:00': 86, '21:45:00': 87, '22:00:00': 88, '22:15:00': 89, '22:30:00': 90, '22:45:00': 91, '23:00:00': 92, '23:15:00': 93, '23:30:00': 94, '23:45:00': 95}

#Mappings Env - Data [Stations]
mapping = {'Aeroporto': 'aeroporto', 'Alameda': 'alameda', 'Alfornelos': 'alfornelos', 'Alto dos Moinhos': 'alto dos moinhos', 'Alvalade': 'alvalade', 'Amadora Este': 'amadora este', 'Ameixoeira': 'ameixoeira', 'Anjos': 'anjos', 'Areeiro': 'areeiro', 'Avenida': 'avenida', 'Baixa Chiado': 'baixa chiado', 'Bela Vista': 'bela vista', 'Cabo Ruivo': 'cabo ruivo', 'Cais do Sodré': 'cais do sodré', 'Campo Grande': 'campo grande', 'Campo Pequeno': 'campo pequeno', 'Carnide': 'carnide', 'Chelas': 'chelas', 'Cidade Universitária': 'cidade universitária', 'Colégio Militar': 'colégio militar', 'Encarnação': 'encarnaçao', 'Entre Campos': 'entre campos', 'Intendente': 'intendente', 'Jardim Zoológico': 'jardim zoológico', 'Laranjeiras': 'laranjeiras', 'Lumiar': 'lumiar', 'Marquês de Pombal': 'marquês de pombal', 'Martim Moniz': 'martim moniz', 'Moscavide': 'moscavide', 'Odivelas': 'odivelas', 'Olaias': 'olaias', 'Olivais': 'olivais', 'Oriente': 'oriente', 'Parque': 'parque', 'Picoas': 'picoas', 'Pontinha': 'pontinha', 'Praça Espanha': 'praça de espanha', 'Quinta das Conchas': 'quinta das conchas', 'Rato': 'rato', 'Reboleira': 'reboleira', 'Restauradores': 'restauradores', 'Roma': 'roma', 'Rossio': 'rossio', 'Saldanha': 'saldanha', 'Santa Apolónia': 'santa apolónia', 'Senhor Roubado': 'sao sebastiao', 'São Sebastião': 'senhor roubado', 'Telheiras': 'telheiras', 'Terreiro Paço': 'terreiro paço'}
inv_mapping = {v: k for k, v in mapping.items()}

endfolder = "../data/models/"

#start running from ~/src !!

class Forecasting:
    def __init__(self):
        self.files_path_count = "../data/parsed_data/data_per_station_count/"
        self.files_path_exit = "../data/parsed_data/data_per_station_exits/"
        self.model_number_of_people = create_model_number_of_people(self.files_path_count)
        self.model_final_station = create_model_final_station(self.files_path_exit)

    def predict_number_of_people(self, station, hour, minutes):
        global date_values

        time = get_closest_15_min_time(hour, minutes)
        time_index = date_values[time]

        base_number = int(round(self.model_number_of_people[mapping[station]][0][time_index]))
        deviation = int(round(self.model_number_of_people[mapping[station]][1][time_index]))
        
        return round(random.randint(max(0, base_number-deviation), base_number+deviation)/15)

    def predict_final_station(self, station, hour, minutes):
        time = get_closest_15_min_time(hour, minutes)

        stations = self.model_final_station[mapping[station]][time][0]
        probabilities = self.model_final_station[mapping[station]][time][1]

        # correction for rounding problem
        if sum(probabilities) > 1:
            probabilities[-1] -=  sum(probabilities) - 1
        elif sum(probabilities) < 1:
            probabilities[-1] +=  1 - sum(probabilities)

        #remove when reboleira added to env model. 
        final = inv_mapping[numpy.random.choice(stations, 1, p=probabilities)[0]]
        while final == 'Reboleira':
            final = inv_mapping[numpy.random.choice(stations, 1, p=probabilities)[0]]

        if same_line(station, final):
            line = get_line_mutual(station, final)
            idx_start = line.index(station)
            idx_final = line.index(final)
            way = idx_start < idx_final
    
        else:
            change = get_line_change(station, final)
            line = get_line_mutual(station, change)
            idx_start = line.index(station)
            idx_final = line.index(change)
            way = idx_start < idx_final

        return final, way


###################################
#
#            AUXILIAR
#
###################################

#only creates the model once. loads from pickle
def create_model_number_of_people(files_path):
    if not os.path.exists(endfolder + 'number_of_people.pickle'):
        result = dict() #{aeroporto: [baricentro, stdevs], ...}

        files = glob.glob(files_path + "*.csv")
        for file in files:
            station = os.path.splitext(os.path.basename(file))[0]

            series = pd.read_csv(file, header=0, parse_dates=[0], index_col=0, squeeze=True)
            df_series = pd.DataFrame(series).sort_index().asfreq('15T', fill_value=0)

            start_date = datetime.datetime(2018, 10, 1)
            end_date = datetime.datetime(2018, 11, 1)

            final_ts = []

            while start_date <= end_date:
                values_by_day = df_series[str(start_date)[:10]]
                arr = values_by_day.to_numpy()
                final_ts.append(arr)
                start_date = start_date + datetime.timedelta(days=1)
                

            barycenter = softdtw_barycenter(final_ts, max_iter=50, tol=1e-3) #array of 96 arrays.

            #Compute the stdev for each hour 
            start_time = datetime.time(0, 0, 0)
            end_time = datetime.time(23, 45, 0)

            std_devs = []

            while start_time < end_time:
                std = df_series.between_time(str(start_time), str(start_time))['count'].to_numpy().std()
                std_devs.append(std)
                start_time = (datetime.datetime.combine(datetime.date(1, 1, 1), start_time) + datetime.timedelta(minutes=15)).time()
            std = df_series.between_time(str(end_time), str(end_time))['count'].to_numpy().std()
            std_devs.append(std)

            result[station] = [list(chain.from_iterable(barycenter.tolist())), std_devs]
        
        with open(endfolder + 'number_of_people.pickle', 'wb') as handle:
            pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
            
        return result
    else:
        with open(endfolder + 'number_of_people.pickle', 'rb') as handle:
            result = pickle.load(handle)
        return result

#huuuuuge dict. lets hope python's dict hash function is decent :D
def create_model_final_station(files_path):
    if not os.path.exists(endfolder + 'final_station.pickle'):
        result = dict()
        files = glob.glob(files_path + "*.csv")
        for file in files:
            station = os.path.splitext(os.path.basename(file))[0]
            result[station] = dict()
            series = pd.read_csv(file, header=0, parse_dates=[0], index_col=0, squeeze=True)
            df_series = pd.DataFrame(series)
            
            start_time = datetime.time(0, 0, 0)
            end_time = datetime.time(23, 45, 0)


            while start_time < end_time:
                stations = df_series.between_time(str(start_time), str(start_time))['estacao_saida'].to_numpy().tolist()
                numbers = df_series.between_time(str(start_time), str(start_time))['count'].to_numpy().tolist()
                
                probability_distribution = [float(n)/sum(numbers) for n in numbers]
                result[station][str(start_time)] = [stations, probability_distribution]

                start_time = (datetime.datetime.combine(datetime.date(1, 1, 1), start_time) + datetime.timedelta(minutes=15)).time()
            
            stations = df_series.between_time(str(end_time), str(end_time))['estacao_saida'].to_numpy().tolist()
            numbers = df_series.between_time(str(end_time), str(end_time))['count'].to_numpy().tolist()

            probability_distribution = [float(n)/sum(numbers) for n in numbers]
            result[station][str(end_time)] = [stations, probability_distribution]  
     
        with open(endfolder + 'final_station.pickle', 'wb') as handle:
                pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return result
    else:
        with open(endfolder + 'final_station.pickle', 'rb') as handle:
            result = pickle.load(handle)
        return result


def get_closest_15_min_time(hour, minute):
    date_time = datetime.datetime(1, 1, 1, hour, minute)
    delta = datetime.timedelta(minutes=15)
    ceil = date_time + (datetime.datetime.min - date_time) % delta 
    return str(ceil.time())


def same_line(s1, s2): 
    for line in [RED, GREEN, BLUE, YELLOW]: 
        if s1 in line and s2 in line: 
            return True 
    return False

def get_line_mutual(station, final):
    for line in [RED, GREEN, BLUE, YELLOW]:
        if station in line and final in line:
            return line

def get_line(station):
    for line in [RED, GREEN, BLUE, YELLOW]:
        if station in line:
            return line

def get_line_change(s1, s2): 
    if same_line(s1, s2) == False: 
        return intersection(get_line(s1), get_line(s2))
    
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3[0]


###################################
#
#              TEST
#
###################################

"""
forecaster = Forecasting()

temp = ['Aeroporto', 'Alameda', 'Alfornelos', 'Alto dos Moinhos', 'Alvalade', 'Amadora Este', 'Ameixoeira', 'Anjos', 'Areeiro', 'Avenida', 'Baixa Chiado', 'Bela Vista', 'Cabo Ruivo', 'Cais do Sodré', 'Campo Grande', 'Campo Pequeno', 'Carnide', 'Chelas', 'Cidade Universitária', 'Colégio Militar', 'Encarnação', 'Entre Campos', 'Intendente', 'Jardim Zoológico', 'Laranjeiras', 'Lumiar', 'Marquês de Pombal', 'Martim Moniz', 'Moscavide', 'Odivelas', 'Olaias', 'Olivais', 'Oriente', 'Parque', 'Picoas', 'Pontinha', 'Praça Espanha', 'Quinta das Conchas', 'Rato', 'Restauradores', 'Roma', 'Rossio', 'Saldanha', 'Santa Apolónia', 'Senhor Roubado', 'São Sebastião', 'Telheiras', 'Terreiro Paço']
#predict alameda 16 horas e 0 minutos.

for i in temp:
    print(forecaster.predict_number_of_people(i, 23, 31))"""


