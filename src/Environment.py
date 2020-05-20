from Orchestrator import Orchestrator
from Line import Line
from Reporter import Reporter

from Forecasting import Forecasting

from Person import Person
from Gui import Gui

import datetime
import time
import random


class Environment:

    def __init__(self):
        self.gui = Gui(self)
        reporter = Reporter(self.gui)
        self.lines = [ Line('red',2, reporter, self.gui) , Line('yellow',2, reporter, self.gui) , Line('blue',2, reporter, self.gui) , Line('green',2, reporter, self.gui) ]
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
        #time.sleep(1)
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


    #Funcao responsavel por adicionar uma pessoa a uma estacao numa troca de linha.
    def add_person_to_station(self, insert_station, line, person):
        for station in line.get_stations():
            if station.get_name() == insert_station:
                print("Station change: ", station.get_name(), " -- ", line.get_color())
                person.reset_entered_time(datetime.time(self.hours, self.minutes))
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
            self.generate_people()
            self.move_trains(self.hours, self.minutes)
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            decisions = self.orchestrator.deliberate()

            print(decisions)
            #exit()

            self.update_lines(decisions)
            self.gui.run()
            self.tik()
            #time.sleep(0.3)

##### Auxiliar

red = ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião']
blue = ['Reboleira', 'Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia']
yellow = ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato']
green = ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
i = 0

forecaster = Forecasting()

def estimate_final_station(station, hours, minutes):
    final = forecaster.predict_final_station(station, hours, minutes)

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

def same_line(s1,s2): 
    for line in [red,green,blue,yellow]: 
        if s1 in line and s2 in line: 
            return True 
    return False

def get_line_mutual(station, final):
    for line in [red,green,blue,yellow]:
        if station in line and final in line:
            return line

def get_line(station):
    for line in [red,green,blue,yellow]:
        if station in line:
            return line

def get_line_change(s1,s2): 
    if(same_line(s1, s2) == False): 
        return intersection(get_line(s1),get_line(s2))


def estimate_number_of_people_per_station(line, hours, minutes):
    estimative = dict()
    for station in line.stations:
        estimative[station.name] = forecaster.predict_number_of_people(station.name, hours, minutes)
    return estimative
    
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3[0]

#may not be necessary
def get_unique_id():
    global i 
    i += 1
    return i
