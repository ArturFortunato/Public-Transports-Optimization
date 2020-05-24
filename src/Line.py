# - coding: utf-8 --
from Modelation.Train import Train
from Modelation.Carriage import Carriage
from Modelation.Station import Station
from Utils.Reporter import Reporter
from Utils.global_vars import init_pos, end_pos, colors, base_carriage_capacity

import datetime
import re



#Initialize all stations
#verde
#arroios ta a mais, nao ha dados
telheiras = Station('Telheiras', 'Telheiras', 'Cais do Sodré', 0, [750, 600], [20, 0], "green")
campo_grande = Station('Campo Grande', 'Telheiras', 'Cais do Sodré', 8, [750, 495], [140, -10], "green")
alvalade = Station('Alvalade', 'Telheiras', 'Cais do Sodré', 20, [750, 450], [-70, -15], "green")
roma = Station('Roma', 'Telheiras', 'Cais do Sodré', 26, [750, 400], [-55, -15], "green")
areeiro = Station('Areeiro', 'Telheiras', 'Cais do Sodré', 33, [750, 350], [-55, -15], "green")
alameda = Station('Alameda', 'Telheiras', 'Cais do Sodré', 40, [750, 300], [15, -25], "green")
#arroios = Station('Arroios', 'Telheiras', 'Cais do Sodré', 44, [750, 260], [-40, -15], "green")
anjos = Station('Anjos', 'Telheiras', 'Cais do Sodré', 48, [750, 220], [-60, -15], "green")
intendente = Station('Intendente', 'Telheiras', 'Cais do Sodré', 53, [750, 180], [-70, -15], "green")
martim_moniz = Station('Martim Moniz', 'Telheiras', 'Cais do Sodré', 60, [750, 150], [-80, -15], "green")
rossio = Station('Rossio', 'Telheiras', 'Cais do Sodré', 65, [750, 120], [-60, -15], "green")
baixa_chiado = Station('Baixa Chiado', 'Telheiras', 'Cais do Sodré', 71, [750, 80], [-135, -10], "green")
cais_do_sodre = Station('Cais do Sodré', 'Telheiras', 'Cais do Sodré', 78, [750, 20], [85, -15], "green")

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('Odivelas', 'Odivelas', 'Rato', 0, [622, 760], [-30, 0], "yellow")
senhor_roubado = Station('Senhor Roubado', 'Odivelas', 'Rato', 4, [646, 708], [-100, -15], "yellow")
ameixoeira = Station('Ameixoeira', 'Odivelas', 'Rato', 10, [670, 656], [-80, -15], "yellow")
lumiar = Station('Lumiar', 'Odivelas', 'Rato', 18, [696, 604], [-60, -15], "yellow")
quinta_conchas = Station('Quinta das Conchas', 'Odivelas', 'Rato', 22, [720, 552], [-110, -15], "yellow")
campo_grande = Station('Campo Grande', 'Odivelas', 'Rato', 31, [750, 495], [0, 0], "yellow", draw=False)
cidade_universitaria = Station('Cidade Universitária', 'Odivelas', 'Rato', 37, [772, 450], [105, -15], "yellow")
entrecampos = Station('Entre Campos', 'Odivelas', 'Rato', 41, [795, 400], [85, -15], "yellow")
campo_pequeno = Station('Campo Pequeno', 'Odivelas', 'Rato', 43, [820, 350], [90, -15], "yellow")
saldanha = Station('Saldanha', 'Odivelas', 'Rato', 51, [845, 300], [110, 0], "yellow")
picoas = Station('Picoas', 'Odivelas', 'Rato', 56, [875, 237], [50, 0], "yellow")
marques_pombal = Station('Marquês de Pombal', 'Odivelas', 'Rato', 59, [905, 175], [160, -15], "yellow")
rato = Station('Rato', 'Odivelas', 'Rato', 68, [982, 20], [20, 0], "yellow")

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]

#vermelha
aeroporto = Station('Aeroporto', 'Aeroporto', 'São Sebastião', 0, [20, 300], [0, 0], "red")
encarnacao = Station('Encarnação', 'Aeroporto', 'São Sebastião', 7, [100, 300], [0, -30], "red")
moscavide = Station('Moscavide', 'Aeroporto', 'São Sebastião', 12, [180, 300], [0, 0], "red")
oriente = Station('Oriente', 'Aeroporto', 'São Sebastião', 20, [250, 300], [0, -30], "red")
cabo_ruivo = Station('Cabo Ruivo', 'Aeroporto', 'São Sebastião', 24, [325, 300], [0, 0], "red")
olivais = Station('Olivais', 'Aeroporto', 'São Sebastião', 29, [400, 300], [0, -30], "red")
chelas = Station('Chelas', 'Aeroporto', 'São Sebastião', 36, [500, 300], [0, 0], "red")
bela_vista = Station('Bela Vista', 'Aeroporto', 'São Sebastião', 41, [600, 300], [0, -30], "red")
olaias = Station('Olaias', 'Aeroporto', 'São Sebastião', 48, [680, 300], [0, 0], "red")
alameda = Station('Alameda', 'Aeroporto', 'São Sebastião', 52, [750, 300], [0, 0], "red", draw=False)
saldanha = Station('Saldanha', 'Aeroporto', 'São Sebastião', 59, [845, 300], [0, 0],"red", draw=False)
sao_sebastiao = Station('São Sebastião', 'Aeroporto', 'São Sebastião', 70, [1115, 300], [130, -15], "red")

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, olaias, alameda, saldanha, sao_sebastiao]

#azul
#missing reboleira
amadora_este = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 0, [1475, 515], [-50, 0], "blue")
alfornelos = Station('Alfornelos', 'Amadora Este', 'Santa Apolónia', 7, [1440, 496], [-70, -15], "blue")
pontinha = Station('Pontinha', 'Amadora Este', 'Santa Apolónia', 16, [1400, 472], [-70, -15], "blue")
carnide = Station('Carnide', 'Amadora Este', 'Santa Apolónia', 21, [1360, 448], [60, -15], "blue")
colegio_militar = Station('Colégio Militar', 'Amadora Este', 'Santa Apolónia', 31, [1315, 420], [80, -15], "blue")
alto_moinhos = Station('Alto dos Moinhos', 'Amadora Este', 'Santa Apolónia', 36, [1275, 396], [90, -15], "blue")
laranjeiras = Station('Laranjeiras', 'Amadora Este', 'Santa Apolónia', 44, [1235, 372], [70, -15], "blue")
jardim_zoologico = Station('Jardim Zoológico', 'Amadora Este', 'Santa Apolónia', 49, [1195, 348], [90, -15], "blue")
praca_espanha = Station('Praça Espanha', 'Amadora Este', 'Santa Apolónia', 58, [1155, 324], [90, -15], "blue")
sao_sebastiao = Station('São Sebastião', 'Amadora Este', 'Santa Apolónia', 68, [1115, 300], [0, 0], "blue", draw=False)
parque = Station('Parque', 'Amadora Este', 'Santa Apolónia', 72, [1010, 237], [70, -15], "blue")
marques_pombal = Station('Marquês de Pombal', 'Amadora Este', 'Santa Apolónia', 77, [905, 175], [0, 0], "blue", draw=False)
avenida = Station('Avenida', 'Amadora Este', 'Santa Apolónia', 79, [854, 144], [-30, 0], "blue")
restauradores = Station('Restauradores', 'Amadora Este', 'Santa Apolónia', 82, [802, 112], [65, -35], "blue")
baixa_chiado = Station('Baixa Chiado', 'Amadora Este', 'Santa Apolónia', 87, [750, 80], [0, 0], "blue", draw=False)
terreio_paço = Station('Terreiro Paço', 'Amadora Este', 'Santa Apolónia', 91, [700, 50], [-85, -15], "blue")
santa_apolonia = Station('Santa Apolónia', 'Amadora Este', 'Santa Apolónia', 98, [650, 20], [-95, -15], "blue")

blue = [amadora_este, alfornelos, pontinha, carnide, colegio_militar, alto_moinhos, laranjeiras, jardim_zoologico, praca_espanha, sao_sebastiao, parque, marques_pombal, avenida, restauradores, baixa_chiado, terreio_paço, santa_apolonia]

lines = {'blue': blue, 'red': red, 'yellow': yellow, 'green': green}

class Line:
    def __init__(self, color, maximum_trains, reporter, gui):
        self.reporter = reporter
        self.color = color
        self.maximum_trains = maximum_trains 
        self.trains = []

        if color == 'red':
            self.stations = red #adiciona metro as 6 e 15 nos dois sentidos
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, red, 1, self.color)]
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, red[::-1], -1, self.color)]
        elif color == 'yellow':
            self.stations = yellow
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, yellow, 1, self.color)]
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, yellow[::-1], -1, self.color)]

        elif color == 'green':
            self.stations = green
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, green, 1, self.color)]
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, green[::-1], -1, self.color)]

        elif color == 'blue':
            self.stations = blue
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, blue, 1, self.color)]
            self.trains += [Train(0, 3, [Carriage(base_carriage_capacity*6, self)], 3, 4, colors[color], gui, blue[::-1], -1, self.color)]
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
        line_info["stations"] = self.stations

        for i in range(len(self.trains)):
            line_info["trains"][i] = self.trains[i].get_train_info()
        return line_info

    def get_train_by_id(self, tid):
        return trains[tid]
        
    def report_satisfaction(self, report, time):
        self.reporter.add_passengers_satisfaction(report, self.color, time)

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

