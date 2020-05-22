from Orchestrator import Orchestrator

from Modelation.Person import Person

from Utils.Forecasting import Forecasting
from Utils.Reporter import Reporter
from Utils.Gui import Gui

from Line import Line

import datetime
import time

class Environment:

    def __init__(self):
        self.gui = Gui(self)
        self.reporter = Reporter(self.gui,1)

        self.lines = [Line('red', 2, self.reporter, self.gui),
                      Line('yellow', 2, self.reporter, self.gui),
                      Line('blue', 2, self.reporter, self.gui),
                      Line('green', 2, self.reporter, self.gui)]
        self.orchestrator = Orchestrator(self.lines)

        self.time = datetime.time(23,15)
        self.day = 1

    #TIME MEASURE
    def tik(self):
        self.time = (datetime.datetime.combine(datetime.date.min, self.time) + datetime.timedelta(minutes = 1)).time()
        if self.time == datetime.time(0,1):
            self.day += 1
            self.reporter.new_day_reset(False,self.orchestrator.get_trains_per_line()) #o orchestrator guarda para o programa correr mais rapido.
            self.reset_passangers_and_trains()
            self.orchestrator.reset()
            self.time = datetime.time(6,15)
            self.gui.run(self.day)
            print("---new day---")
            time.sleep(10)
            #current behaviour: All trains and people in station at midnight and 1 minute are deleted
            #may be todo: dont generate more trains at 0h01, dont generate more people, but let the remaining trains finish the trip
            #people not picked up by the final trip are then deleted


    #EVENTS
    def move_trains(self):
        for line in self.lines:
            passengers_to_exchange = line.move_trains(self.time)
            if passengers_to_exchange != {}:
                self.change_passengers_line(passengers_to_exchange)

    def generate_people(self):
        for line in self.lines:
            self.populate_stations(line)

    def reset_passangers_and_trains(self):
        for line in self.lines:
            line.percept_new_day()
    
    def update_lines(self, decisions):
        for line in self.lines:
            line.update_line_info(decisions[line.color])

    #AUXILIAR

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
        return None

    def get_mutual_station_line(self, station1, station2):
        line = self.get_stations_line(station1, station2)
        if line != None:
            return True, line
        else:
            return False, None

    #Funcao responsavel por adicionar uma pessoa a uma estacao numa troca de linha.
    def add_person_to_station(self, insert_station, line, person):
        for station in line.get_stations():
            if station.get_name() == insert_station:
                #print("Station change: ", station.get_name(), " -- ", line.get_color())
                person.reset_entered_time(self.time)
                station.add_person(person)
                break

    def change_passengers_line(self, passengers_to_exchange):
        for station in passengers_to_exchange:
            for person in passengers_to_exchange[station]:
                line = self.get_stations_line(person.get_final_station(), station)
                person.update_way(line, station)
                self.add_person_to_station(station, line, person)

    # receives a Line object
    def populate_stations(self, line):
        stations_distribution = estimate_number_of_people_per_station(line, self.time)
        #{oriente: 2, encarnacao: 3, .... }
        for station in stations_distribution:
            for number_of_persons in range(stations_distribution[station]):
                final, way = estimate_final_station(station, self.time)
                is_same_line, same_line = self.get_mutual_station_line(station, final)
                if is_same_line and same_line != line:
                    #examplo: estamos a adicionar a sao sebastiao vermelho. Se sai marques, entao ele vai por em S.Sebastiao Red -> marques. Devia estar no blue.
                    continue
                person = Person(station, final, self.time, way)
                line.percept_person_in_station(person, station)


    def run(self):
        try:
            while True:
                self.generate_people()

                self.move_trains()
                self.orchestrator.percept(self.time.hour, self.time.minute)
                decisions = self.orchestrator.deliberate()
                self.update_lines(decisions)

                self.gui.run(self.day)

                self.tik()
        except KeyboardInterrupt:
            print("Deste Ctrl-c.")
            self.reporter.generate_charts(True)
            exit()

##### Auxiliar
pid = 0
forecaster = Forecasting()

def estimate_final_station(station, time):
    final, way = forecaster.predict_final_station(station, time)
    return final, way

def estimate_number_of_people_per_station(line, time):
    estimative = dict()
    for station in line.stations:
        estimative[station.name] = forecaster.predict_number_of_people(station.name, time)
    return estimative

def get_unique_id():
    global pid 
    pid += 1
    return pid
