from Orchestrator import Orchestrator
from Line import Line
from Reporter import Reporter

from Person import Person
from Gui import Gui

import datetime
import time
import random


class Environment:

    def __init__(self):
        self.gui = Gui(self)
        reporter = Reporter(self.gui)
        self.lines = [ Line('red',2,[], reporter, self.gui) , Line('yellow',2,[], reporter, self.gui) , Line('blue',2,[], reporter, self.gui) , Line('green',2,[], reporter, self.gui) ]
        self.orchestrator = Orchestrator(self.lines)
        self.day_ended = False
        self.start_day()

    def start_day(self):
        self.hours = 6
        self.minutes = 15
    
    def tik(self):
        if self.minutes != 59:
            self.minutes += 1
        else:
            self.minutes = 0 
            self.hours = (self.hours + 1) % 24

            if self.hours == 1:
                self.day_ended = True

    def add_change_passengers_to_line(self, current_station, line, passengers_to_exchange):
        for station in line.get_stations():
            print(station.get_name(), current_station.get_name())
            if station.get_name() == current_station.get_name():
                for passenger in passengers_to_exchange:
                    passenger.update_way(line, station)
                    station.addPerson(passenger)
                return True
        time.sleep(1)
        return False

    # returns the only line that has both station1 and station2
    def get_stations_line(self, station1, station2):
        for line in self.lines:
            cont = 0
            for station in line.get_stations():
                if station.get_name() == station1:
                    cont += 1
                elif station.get_name() == station2:
                    cont += 1
            if cont == 2:
                return line

    def add_person_to_station(self, insert_station, line, person):
        for station in line.get_stations():
            if station.get_name() == insert_station:
                print("Station change: ", station.get_name(), " -- ", line.get_color())
                station.addPerson(person)
                break

    def change_passengers_line(self, passengers_to_exchange):
        for station in passengers_to_exchange:
            for person in passengers_to_exchange[station]:
                line = self.get_stations_line(person.get_final_station(), station)
                person.update_way(line, station)
                self.add_person_to_station(station, line, person)

    def move_trains(self, hours, minutes):
        for line in self.lines:
            passengers_to_exchange = line.move_trains(hours, minutes)
            if passengers_to_exchange != {}:
                self.change_passengers_line(passengers_to_exchange)

    def generate_people(self):
        for line in self.lines:
            self.populate_stations(line)

    # receives a Line object
    def populate_stations(self, line):
        stationsDistribution = estimate_number_of_people_per_station(line, self.hours, self.minutes)
        #{oriente: 2, encarnacao: 3, .... }
        for station in stationsDistribution:
            for number_of_persons in range(stationsDistribution[station]):
                final, way = estimate_final_station(station, self.hours, self.minutes)
                p = Person(get_unique_id(), station, final, datetime.time(self.hours, self.minutes), way)
                line.add_person_to_station(p, station)


    def update_lines(self, decisions):
        for line in self.lines:
            line.update_line_info(decisions[line.color])

    #person to test line change!! make sure that line changes are occuring before continuing
    def hardcode_new_person(self):
        p = Person ("Zé", "Laranjeiras", "Rato" ,datetime.time(self.hours, self.minutes), True)
        self.lines[2].add_person_to_station(p, "Laranjeiras")
        
    def run(self):
        self.hardcode_new_person()
        while True:
            #self.generate_people()
            self.move_trains(self.hours, self.minutes)
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            decisions = self.orchestrator.deliberate()
            self.update_lines(decisions)
            self.gui.run()
            self.tik()
            time.sleep(0.3)

##### Auxiliar

#rethink station and line design if this seems too ugly
red = ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião']
blue = ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia']
yellow = ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato']
green = ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
i = 0


#mudanca de linha
mudanca_linha = ["São Sebastião","Marquês de Pombal","Saldanha","Baixa Chiado","Alameda","Campo Grande"]

stations_per_line = {
    "red": ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião'],
    "blue": ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia'],
    "yellow": ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato'],
    "green": ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
}

""" def format_hour(hours,minutes):
    end_quarter = minutes + 15
    hr = str(hours)
    mn = str(minutes)

    if(len(str(hours)) == 1):
        hr = str(0) + str(hours)
        #hora_formatada =  str(0) + str(hours) + ":" + str(minutes) + "-" + str(end_quarter)
    if(len(str(minutes)) == 1):
        mn = str(0) + str(minutes)
   
    hora_formatada = hr + ":" + mn + "-" + str(end_quarter)
    return hora_formatada


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

        hora_formatada = format_hour(hours,minutes)
        line_stations = stations_per_line[line] #remove a estacao atual

        dic_stations = {}
        counter = 0
        for s in line_stations:
            if(s != station):
                dic_stations[s] = sg.extract_value(line,hora_formatada,s,"entradas")
                counter += dic_stations[s]

        #normalizacao
        for key in list(dic_stations.keys()):
            dic_stations[key] = dic_stations[key] / counter

        counter = 0 
        prob = random.uniform(0, 1)

        for key in list(dic_stations.keys()):
            counter += dic_stations[key]
            if(counter >= prob):
                return key



#TODO: analyse the data
#toy example with random number for each station
def estimate_number_of_people_per_station(line, hours, minutes):
    estimative = dict()
    print(hours)
    print(minutes)
    for station in line.stations:
        hora_formatada = format_hour(hours,minutes)
        estimative[station.name] = sg.extract_value(line.color,hora_formatada,station.name,"entradas") """


#this is ugly but it'll change when we have the models of the data so dw
def estimate_final_station(station, hours, minutes):
    if station in red:
        temp = list(filter(lambda x: x != station,red))
        final = random.choice(temp)
        idx_start = red.index(station)
        idx_final = red.index(final)
        way = idx_start < idx_final
        return final,way
    if station in blue:
        temp = list(filter(lambda x: x != station,blue))
        final = random.choice(temp)
        idx_start = blue.index(station)
        idx_final = blue.index(final)
        way = idx_start < idx_final
        return final,way
    if station in green:
        temp = list(filter(lambda x: x != station,green))
        final = random.choice(temp)
        idx_start = green.index(station)
        idx_final = green.index(final)
        way = idx_start < idx_final
        return final,way
    if station in yellow:
        temp = list(filter(lambda x: x != station,yellow))
        final = random.choice(temp)
        idx_start = yellow.index(station)
        idx_final = yellow.index(final)
        way = idx_start < idx_final
        return final,way


#TODO: analyse the data
#toy example with random number for each station
def estimate_number_of_people_per_station(line, hours, minutes):
    estimative = dict()
    for station in line.stations:
        estimative[station.name] = random.randint(1,1)
    return estimative
    
#may not be necessary
def get_unique_id():
    global i 
    i += 1
    return i


