# - coding: utf-8 --

from Modelation.Train import Train
from Modelation.Carriage import Carriage
from Utils.Reporter import Reporter
from Utils.global_vars import lines, red, blue, green, yellow
from Utils.global_vars import init_pos, end_pos, colors, base_carriage_capacity

import datetime
import re

class Line:
    def __init__(self, color, maximum_trains, reporter, gui):
        self.reporter = reporter
        self.color = color
        self.maximum_trains = maximum_trains 
        self.trains = []

        if color == 'red':
            self.stations = red
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, red[::-1], -1, self.color)]
        elif color == 'yellow':
            self.stations = yellow
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, yellow, 1, self.color)]
        elif color == 'green':
            self.stations = green
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, green, 1, self.color)]
        elif color == 'blue':
            self.stations = blue
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 1, 4, colors[color], gui, blue, 1, self.color)]
        self.number_of_trains = 1
        
        #gui stuff
        self.gui = gui
        self.gui.add_line(self)
        for i in range(len(self.stations)):
            self.stations[i].set_gui(gui)

    
    ####################################
    #
    #            ACTIONS
    #
    ####################################

    #hardcoded 6 carriaged with 185 capacity each
    def add_train(self, info):
        carriages = []
        #for i in range(info['nr_carriages']):
        carriages.append(Carriage(185*6, self))

        if info["way"] == 1: line_stations = lines[self.color]
        else: line_stations = lines[self.color][::-1]            


        self.trains += [Train(self.number_of_trains, 3, carriages, 6, 4, colors[self.color], self.gui, line_stations, info['way'], self.color)]
        self.number_of_trains += 1

    
    def move_trains(self, time):
        passengers_to_exchange = {}
        trains_to_remove = []

        for train in self.trains:
            for station in self.stations:
                if station.get_position() == train.get_position():
                    passengers_to_enter = station.get_persons(train.get_way())
                    people_boarded, passengers_to_exchange_temp, report = train.open_doors(station, passengers_to_enter, time)
                    # needs to know the station where the exchange happens to transfer people to the new platform
                    if passengers_to_exchange_temp != []:
                        if station in passengers_to_exchange:
                            print("DAFUC?")
                            exit()
                        passengers_to_exchange[station.get_name()] = passengers_to_exchange_temp
                    station.remove_persons_until_index(people_boarded, train.get_way())
                    self.report_satisfaction(report, time)
                    
                    avg_train_occupancy = self.avg_train_capacity()
                    self.reporter.report_average_train_occupancy(self.color,avg_train_occupancy)

                    # se tiver chegado a estacao final (ou "inicial" se estiver a andar ao contrario, adiciona o comboio à lista de comboios para apagar)
                    if station == self.stations[-1 if train.get_way() == 1 else 0]:
                        trains_to_remove += [train]
        self.delete_trains(trains_to_remove)

        for i in range(len(self.trains)):
            self.trains[i].move()

        return passengers_to_exchange


    ####################################
    #
    #            SENSORS
    #
    ####################################
    def percept_new_day(self):
        for station in self.stations:
            station.reset()
        self.delete_trains(self.trains)

    def percept_person_in_station(self, person, station):
        for s in self.stations:
            if s.name == station:
                s.add_person(person)

    #information provided by the orchestrator
    def update_trains_info(self, deliberations):
        for i in range(len(self.trains)):
            if i in deliberations:
                self.trains[i].update_train_info(deliberations[i])

    def update_line_info(self, deliberations):
        if 'trains' in deliberations:
            self.update_trains_info(deliberations['trains'])
        if 'new_train' in deliberations:
            for i in range(len(deliberations['new_train'])):
                self.add_train(deliberations['new_train'][i])

    ####################################
    #
    #            AUXILIAR
    #
    ####################################
    def delete_trains(self, trains_to_remove):
        for train_to_delete in trains_to_remove:
            for i in range(len(self.trains)):
                if train_to_delete.get_id() == self.trains[i].get_id():
                    self.gui.delete_train(self.trains[i])
                    #del self.trains[i]
                    #del may break the indexes if more than one i and the one that matches the if is not the 1st
                    #but plz check if this is the desired behaviour
                    self.trains = [train for train in self.trains if self.trains.index(train) != i]
                    break

    def can_update_train_speed(self, current_train, position, new_speed):
        for train in self.trains:  
            if train.get_way() == current_train.get_way() and train.get_id() < current_train.get_id() and (position + new_speed) >= (train.get_position() + train.get_speed()):
                return False
        return True

    def avg_train_capacity(self):
        train_occupancy_ratio = []
        for train in self.trains:
            for carriage in train.carriages:
                train_occupancy_ratio.append(carriage.get_occupancy_ratio())
        return sum(train_occupancy_ratio)/ len(train_occupancy_ratio)
    
    def get_line_info(self):
        line_info = {}
        line_info["trains"] = {}
        for i in range(len(self.trains)):
            line_info["trains"][i] = self.trains[i].get_train_info()
            line_info["stations"] = self.stations
        return line_info

    def get_train_by_id(self, tid):
        return trains[tid]
        
    def report_satisfaction(self, report, time):
        self.reporter.add_passengers_satisfaction(report,self.color, time)

    def init_pos(self):
        return init_pos[self.color]

    def end_pos(self):
        return end_pos[self.color]

    def get_color(self):
        return self.color

    def get_stations(self):
        return self.stations

    def get_id(self):
        return self.color

