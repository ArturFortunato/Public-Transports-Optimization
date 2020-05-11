from Orchestrator import Orchestrator
from Line import Line
from Reporter import Reporter

import Schedule_Getter as sg
from Person import Person

import time
import random


class Environment:

    def __init__(self):
        reporter = Reporter()
        self.lines = [ Line('red',2,[], reporter) , Line('yellow',2,[], reporter) , Line('blue',2,[], reporter) , Line('green',2,[], reporter) ]
        self.orchestrator = Orchestrator(self.lines)
        self.day_ended = False
        self.start_day()

    def start_day(self):
        self.hours = 6
        self.minutes = 0
    
    def tik(self):
        if self.minutes != 59:
            self.minutes += 1
        else:
            self.minutes = 0 
            self.hours = (self.hours + 1) % 24

            if self.hours == 1:
                self.day_ended = True

    def move_trains(self):
        for line in self.lines:
            line.move_trains()
        
    def generate_people(self):
        for line in self.lines:
                self.populate_stations(line)

    # receives a Line object
    def populate_stations(self, line):
        stationsDistribution = estimate_number_of_people_per_station(line, self.hours, self.minutes)
        #{oriente: 2, encarnacao: 3, .... }
        for station in stationsDistribution:
            for number_of_persons in range(stationsDistribution[station]): 
                p = Person(get_unique_id(), station, estimate_final_station(station,line.color, self.hours, self.minutes))
                line.add_person_to_station(p, station)


    def run(self):
        while True:
            self.generate_people()
            self.move_trains()
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            self.orchestrator.deliberate()
            self.orchestrator.actuate()
            self.tik()
            print("TIK")
            time.sleep(1)




##### Auxiliar

#rethink station and line design if this seems too ugly
red = ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Alameda', 'Saldanha', 'São Sebastião']
blue = ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal 1', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Amadora Este']
yellow = ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato']
green = ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
i = 0



#mudanca de linha
mudanca_linha = ["São Sebastião","Marquês de Pombal","Saldanha","Baixa Chiado","Alameda","Campo Grande"]

stations_per_line = {
    "red": ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Alameda', 'Saldanha', 'São Sebastião'],
    "blue": ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal 1', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Amadora Este'],
    "yellow": ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato'],
    "green": ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
}

#TODO: analyse the data
#toy example with random station
#-entrance station
#-return a string 
#Outputs a destination station for a person.
def estimate_final_station(line,station, hours, minutes):
    prob = random.uniform(0, 1)

    if(prob >= 0.90):#mudanca de linha
        valid_stations = []
        for s in stations_per_line.keys():
            if(s != line):
                valid_stations = valid_stations + stations_per_line[s]
        valid_stations = set(valid_stations)
        if(station in valid_stations):
            valid_stations.remove(list(station))
        return random.choice(list(valid_stations))

    else:#calcula probabilide de sair numa estacao da mesma linha
        end_quarter = minutes + 15

        if(len(str(hours)) == 1):
            hora_formatada =  str(0) + str(hours) + ":" + str(minutes) + "-" + str(end_quarter)
        else:
            hora_formatada = str(hours) + ":" + str(minutes) + "-" + str(end_quarter)


        line_stations = stations_per_line[line] #remove a estacao atual

        dic_stations = {}
        counter = 0
        for s in line_stations:
            if(s != station):
                print("o valor da hora_formatada e: " + str(hora_formatada))
                print("o valor de s e: " + str(s))
                dic_stations[s] = sg.extract_value(line,hora_formatada,s,"entradas")
                counter += dic_stations[s]
            #print(s)

    #if station in red:
    #    return random.choice(red)


#TODO: analyse the data
#toy example with random number for each station
def estimate_number_of_people_per_station(line, hours, minutes):
    estimative = dict()
    for station in line.stations:
        estimative[station.name] = random.randint(1,10)
    return estimative

#may not be necessary
def get_unique_id():
    global i 
    i += 1
    return i


print(estimate_final_station("yellow", "Rato",7,45))