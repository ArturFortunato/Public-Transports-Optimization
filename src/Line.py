# - coding: utf-8 --

from Station import Station
from Reporter import Reporter
from Train import Train
from Carriage import Carriage


import datetime
import re

#verde
#arroios ta a mais, nao ha dados
telheiras = Station('Telheiras', 'Telheiras', 'Cais do Sodré', 0, [750, 600], [0, 0])
campo_grande = Station('Campo Grande', 'Telheiras', 'Cais do Sodré', 8, [750, 495], [70,-10])
alvalade = Station('Alvalade', 'Telheiras', 'Cais do Sodré', 20, [750, 450], [-40, -15])
roma = Station('Roma', 'Telheiras', 'Cais do Sodré', 26, [750, 400], [-35, -15])
areeiro = Station('Areeiro', 'Telheiras', 'Cais do Sodré', 33, [750, 350], [-35, -15])
alameda = Station('Alameda', 'Telheiras', 'Cais do Sodré', 40, [750, 300], [35, -25])
arroios = Station('Arroios', 'Telheiras', 'Cais do Sodré', 44, [750, 260], [-40, -15])
anjos = Station('Anjos', 'Telheiras', 'Cais do Sodré', 48, [750, 220], [-30, -15])
intendente = Station('Intendente', 'Telheiras', 'Cais do Sodré', 53, [750, 180], [-50, -15])
martim_moniz = Station('Martim Moniz', 'Telheiras', 'Cais do Sodré', 60, [750, 150], [-60, -15])
rossio = Station('Rossio', 'Telheiras', 'Cais do Sodré', 65, [750, 120], [-40, -15])
baixa_chiado = Station('Baixa Chiado', 'Telheiras', 'Cais do Sodré', 71, [750, 80], [65, -15])
cais_do_sodre = Station('Cais do Sodré', 'Telheiras', 'Cais do Sodré', 78, [750, 20], [65, -15])

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, arroios, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('Odivelas', 'Odivelas', 'Rato', 0, [622, 760], [-30, 0])
senhor_roubado = Station('Senhor Roubado', 'Odivelas', 'Rato', 4, [646, 708], [-80, -15])
ameixoeira = Station('Ameixoeira', 'Odivelas', 'Rato', 10, [670, 656], [-60, -15])
lumiar = Station('Lumiar', 'Odivelas', 'Rato', 18, [696, 604], [-40, -15])
quinta_conchas = Station('Quinta das Conchas', 'Odivelas', 'Rato', 22, [720, 552], [-90, -15])
campo_grande = Station('Campo Grande', 'Odivelas', 'Rato', 31, [750, 495], [0, 0], False)
cidade_universitaria = Station('Cidade Universitária', 'Odivelas', 'Rato', 37, [772, 450], [85, -15])
entrecampos = Station('Entre Campos', 'Odivelas', 'Rato', 41, [795, 400], [65, -15])
campo_pequeno = Station('Campo Pequeno', 'Odivelas', 'Rato', 43, [820, 350], [70, -15])
saldanha = Station('Saldanha', 'Odivelas', 'Rato', 51, [845, 300], [40, 0])
picoas = Station('Picoas', 'Odivelas', 'Rato', 56, [875, 237], [30, 0])
marques_pombal = Station('Marquês de Pombal', 'Odivelas', 'Rato', 59, [905,175], [90, -20])
rato = Station('Rato', 'Odivelas', 'Rato', 68, [982, 20], [20, 0])

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]


#vermelha
aeroporto = Station('Aeroporto', 'Aeroporto', 'São Sebastião', 0, [20, 300], [0, 0])
encarnacao = Station('Encarnação', 'Aeroporto', 'São Sebastião', 7, [100, 300], [0, -30])
moscavide = Station('Moscavide', 'Aeroporto', 'São Sebastião', 12, [180, 300], [0, 0])
oriente = Station('Oriente', 'Aeroporto', 'São Sebastião', 20, [250, 300], [0, -30])
cabo_ruivo = Station('Cabo Ruivo', 'Aeroporto', 'São Sebastião', 24, [325, 300], [0, 0])
olivais = Station('Olivais', 'Aeroporto', 'São Sebastião', 29, [400, 300], [0, -30])
chelas = Station('Chelas', 'Aeroporto', 'São Sebastião', 36, [500, 300], [0, 0])
bela_vista = Station('Bela Vista', 'Aeroporto', 'São Sebastião', 41, [600, 300], [0, -30])
olaias = Station('Olaias', 'Aeroporto', 'São Sebastião', 48, [680, 300], [0, 0])
alameda = Station('Alameda', 'Aeroporto', 'São Sebastião',52, [750, 300], [0, 0], False)
saldanha = Station('Saldanha', 'Aeroporto', 'São Sebastião', 59, [845, 300], [0, 0], False)
sao_sebastiao = Station('São Sebastião', 'Aeroporto', 'São Sebastião', 70, [1115, 300], [70, -15])

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, olaias, alameda, saldanha, sao_sebastiao]

#azul
#missing reboleira
amadora_este = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 0, [1475, 515], [-50, 0])
alfornelos = Station('Alfornelos', 'Amadora Este', 'Santa Apolónia', 7, [1440, 496], [-50, -15])
pontinha = Station('Pontinha', 'Amadora Este', 'Santa Apolonia', 16, [1400, 472], [50, -15])
carnide = Station('Carnide', 'Amadora Este', 'Santa Apolónia', 21, [1360, 448], [50, -15])
colegio_militar = Station('Colégio Militar', 'Amadora Este', 'Santa Apolónia', 31, [1315, 420], [70, -15])
alto_moinhos = Station('Alto dos Moinhos', 'Amadora Este', 'Santa Apolónia', 36, [1275, 396], [80, -15])
laranjeiras = Station('Laranjeiras', 'Amadora Este', 'Santa Apolónia', 44, [1235, 372], [60, -15])
jardim_zoologico = Station('Jardim Zoológico', 'Amadora Este', 'Santa Apolónia', 49, [1195, 348], [80, -15])
praca_espanha = Station('Praça Espanha', 'Amadora Este', 'Santa Apolónia', 58, [1155, 324], [80, -15])
sao_sebastiao = Station('São Sebastião', 'Amadora Este', 'Santa Apolónia', 68, [1115, 300], [0, 0], False)
parque = Station('Parque', 'Amadora Este', 'Santa Apolónia', 72, [1010, 237], [-20, 0])
marques_pombal = Station('Marquês de Pombal', 'Amadora Este', 'Santa Apolónia', 77, [905,175], [0, 0], False)
avenida = Station('Avenida', 'Amadora Este', 'Santa Apolónia', 79, [854, 144], [-30, 0])
restauradores = Station('Restauradores', 'Amadora Este', 'Santa Apolónia', 82, [802, 112], [65, -15])
baixa_chiado = Station('Baixa Chiado', 'Amadora Este', 'Santa Apolónia', 87, [750, 80], [0, 0], False)
terreio_paço = Station('Terreiro Paço', 'Amadora Este', 'Santa Apolónia', 91, [700, 50], [-65, -15])
santa_apolonia = Station('Santa Apolónia', 'Amadora Este', 'Santa Apolónia', 98, [650, 20], [-65, -15])

blue = [amadora_este, alfornelos, pontinha, carnide, colegio_militar, alto_moinhos, laranjeiras, jardim_zoologico, praca_espanha, sao_sebastiao, parque, marques_pombal, avenida, restauradores, baixa_chiado, terreio_paço, santa_apolonia]

lines = {'blue': blue, 'red': red, 'yellow': yellow, 'green': green}

init_pos = {
    'red': [20, 300],
    'green': [750, 20],
    'blue': [650, 20],
    'yellow': [620, 760]
}

end_pos = {
    'red': [1115, 300],
    'green': [750, 600],
    'blue': [1475, 515],
    'yellow': [980, 20]
}

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0)
}

class Line:
    def __init__(self, color, maximum_trains, trains, reporter, gui):
        self.reporter = reporter
        self.color = color #string #considered id
        self.maximum_trains = maximum_trains 
        self.trains = trains #dictionary of trains
        self.number_of_trains = len(trains)

        #Todas as linhas excepto a azul tiveram a sua velocidade aumentada.
        if color == 'red':
            self.stations = red
            self.trains += [Train(0, 3, [Carriage(80, self)], 3, 4, colors[color], gui, red[::-1], -1, self.color)]
        elif color == 'yellow':
            self.stations = yellow
            self.trains += [Train(0, 3, [Carriage(80, self)], 3, 4, colors[color], gui, yellow, 1, self.color)]
        elif color == 'green':
            self.stations = green
            self.trains += [Train(0, 3, [Carriage(80, self)], 3, 4, colors[color], gui, green, 1, self.color)]
        elif color == 'blue':
            self.stations = blue
            self.trains += [Train(0, 3, [Carriage(80, self)], 1, 4, colors[color], gui, blue, 1, self.color)]

        #gui stuff
        self.gui = gui
        self.gui.add_line(self)
        for i in range(len(self.stations)):
            self.stations[i].set_gui(gui)


    def get_id(self):
        return self.color

    def getStation(self, name):
        for station in self.stations:
            if station.name == name:
                return station


    def get_stations(self):
        return self.stations

    def move_trains(self, hours, minutes):
        passengers_to_exchange = {}
        for i in range(len(self.trains)):
            self.trains[i].move()

        for train in self.trains:
            for station in self.stations:
                if station.get_position() == train.get_position():
                    passengers_to_enter = station.get_persons(train.get_way())
                    people_boarded, passengers_to_exchange_temp, report = train.open_doors(station, passengers_to_enter, datetime.time(hours, minutes))
                    # needs to know the station where the exchange happens to transfer people to the new platform
                    if passengers_to_exchange_temp != []:
                        if station in passengers_to_exchange:
                            print("DAFUC?")
                            exit()
                        passengers_to_exchange[station.get_name()] = passengers_to_exchange_temp
                    station.remove_persons_until_index(people_boarded, train.get_way())
                    self.report_satisfaction(report)
        return passengers_to_exchange


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

    def get_line_info(self):
        line_info = {}
        line_info["trains"] = {}
        for i in range(len(self.trains)):
            line_info["trains"][i] = self.trains[i].get_train_info()
            line_info["stations"] = self.stations
        return line_info

    def get_train_by_id(self, tid):
        return trains[tid]
        
    def report_satisfaction(self, report):
        self.reporter.add_passengers_satisfaction(report)

    #need to change stations representations from list to dict, to avoid the for loop.
    def add_person_to_station(self, person, station):
        for s in self.stations:
            if s.name == station:
                s.addPerson(person)

    def init_pos(self):
        return init_pos[self.color]

    def end_pos(self):
        return end_pos[self.color]

    def get_color(self):
        return self.color
    
    def add_train(self, info):
        carriages = []
        for i in range(info['nr_carriages']):
            carriages.append(Carriage(80, self))

        if info["way"] == 1: line_color = lines[self.color]

        else: line_color = lines[self.color][::1]            

        self.trains += [Train(len(self.trains), 3, carriages, info['nr_carriages'], 4, colors[self.color], self.gui, line_color, info['way'], self.color )]


