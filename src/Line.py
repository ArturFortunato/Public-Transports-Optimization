
from Station import Station
from Reporter import Reporter

import re

#verde
telheiras = Station('Telheiras', 'Telheiras', 'Cais do Sodré', 0, [750, 650])
campo_grande = Station('Campo Grande', 'Telheiras', 'Cais do Sodré', 8, None)
alvalade = Station('Alvalade', 'Telheiras', 'Cais do Sodré', 20, None)
roma = Station('Roma', 'Telheiras', 'Cais do Sodré', 26, None)
areeiro = Station('Areeiro', 'Telheiras', 'Cais do Sodré', 33, None)
alameda = Station('Alameda', 'Telheiras', 'Cais do Sodré', 40, None)
arroios = Station('Arroios', 'Telheiras', 'Cais do Sodré', 44, None)
anjos = Station('Anjos', 'Telheiras', 'Cais do Sodré', 48, None)
intendente = Station('Intendente', 'Telheiras', 'Cais do Sodré', 53, None)
martim_moniz = Station('Martim Moniz', 'Telheiras', 'Cais do Sodré', 60, None)
rossio = Station('Rossio', 'Telheiras', 'Cais do Sodré', 65, None)
baixa_chiado = Station('Baixa Chiado', 'Telheiras', 'Cais do Sodré', 71, None)
cais_do_sodre = Station('Cais do Sodré', 'Telheiras', 'Cais do Sodré', 78, [750, 20])

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, arroios, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('Odivelas', 'Odivelas', 'Rato', 0, [650, 700])
senhor_roubado = Station('Senhor Roubado', 'Odivelas', 'Rato', 4, None)
ameixoeira = Station('Ameixoeira', 'Odivelas', 'Rato', 10, None)
lumiar = Station('Lumiar', 'Odivelas', 'Rato', 18, None)
quinta_conchas = Station('Quinta das Conchas', 'Odivelas', 'Rato', 22, None)
campo_grande = Station('Campo Grande', 'Odivelas', 'Rato', 31, None)
cidade_universitaria = Station('Cidade Universitária', 'Odivelas', 'Rato', 37, None)
entrecampos = Station('Entre Campos', 'Odivelas', 'Rato', 41, None)
campo_pequeno = Station('Campo Pequeno', 'Odivelas', 'Rato', 43, None)
saldanha = Station('Saldanha', 'Odivelas', 'Rato', 51, None)
picoas = Station('Picoas', 'Odivelas', 'Rato', 56, None)
marques_pombal = Station('Marquês de Pombal', 'Odivelas', 'Rato', 59, None)
rato = Station('Rato', 'Odivelas', 'Rato', 68, [980, 20])

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]


#vermelha
aeroporto = Station('Aeroporto', 'Aeroporto', 'São Sebastião', 0, [20, 300])
encarnacao = Station('Encarnação', 'Aeroporto', 'São Sebastião', 7, None)
moscavide = Station('Moscavide', 'Aeroporto', 'São Sebastião', 12, None)
oriente = Station('Oriente', 'Aeroporto', 'São Sebastião', 20, None)
cabo_ruivo = Station('Cabo Ruivo', 'Aeroporto', 'São Sebastião', 24, None)
olivais = Station('Olivais', 'Aeroporto', 'São Sebastião', 29, None)
chelas = Station('Chelas', 'Aeroporto', 'São Sebastião', 36, None)
bela_vista = Station('Bela Vista', 'Aeroporto', 'São Sebastião', 41, None)
olaias = Station('Olaias', 'Aeroporto', 'São Sebastião', 48, None)
alameda = Station('Alameda', 'Aeroporto', 'São Sebastião',52, None)
saldanha = Station('Saldanha', 'Aeroporto', 'São Sebastião', 59, None)
sao_sebastiao = Station('São Sebastião', 'Aeroporto', 'São Sebastião', 70, [980, 300])

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, alameda, saldanha, sao_sebastiao]

#azul
amadora_este = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 0, [1450, 700])
alfornelos = Station('Alfornelos', 'Amadora Este', 'Santa Apolónia', 7, None)
pontinha = Station('Pontinha', 'Amadora Este', 'Santa Apolonia', 16, None)
carnide = Station('Carnide', 'Amadora Este', 'Santa Apolónia', 21, None)
colegio_militar = Station('Colégio Militar', 'Amadora Este', 'Santa Apolónia', 31, None)
alto_moinhos = Station('Alto dos Moinhos', 'Amadora Este', 'Santa Apolónia', 36, None)
laranjeiras = Station('Laranjeiras', 'Amadora Este', 'Santa Apolónia', 44, None)
jardim_zoologico = Station('Jardim Zoológico', 'Amadora Este', 'Santa Apolónia', 49, None)
praca_espanha = Station('Praça Espanha', 'Amadora Este', 'Santa Apolónia', 58, None)
sao_sebastiao = Station('São Sebastião', 'Amadora Este', 'Santa Apolónia', 68, [980, 300])
parque = Station('Parque', 'Amadora Este', 'Santa Apolónia', 72, None)
marques_pombal = Station('Marquês de Pombal 1', 'Amadora Este', 'Santa Apolónia', 77, None)
avenida = Station('Avenida', 'Amadora Este', 'Santa Apolónia', 79, None)
restauradores = Station('Restauradores', 'Amadora Este', 'Santa Apolónia', 82, None)
baixa_chiado = Station('Baixa Chiado', 'Amadora Este', 'Santa Apolónia', 87, None)
terreio_paço = Station('Terreiro Paço', 'Amadora Este', 'Santa Apolónia', 91, None)
santa_apolonia = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 98, [650, 20])

blue = [amadora_este, alfornelos, pontinha, carnide, colegio_militar, alto_moinhos, laranjeiras, jardim_zoologico, praca_espanha, sao_sebastiao, parque, marques_pombal, avenida, restauradores, baixa_chiado, terreio_paço, santa_apolonia]

init_pos = {
    'red': [20, 300],
    'green': [750, 20],
    'blue': [650, 20],
    'yellow': [650, 700]
}

end_pos = {
    'red': [980, 300],
    'green': [750, 650],
    'blue': [1450, 700],
    'yellow': [980, 20]
}

class Line:
    def __init__(self, color, maximum_trains, trains, reporter, gui):
        self.reporter = reporter
        self.color = color #string #considered id
        self.maximum_trains = maximum_trains 
        self.trains = trains #dictionary of trains
        self.number_of_trains = len(trains)
        if color == 'red':
            self.stations = red
        elif color == 'yellow':
            self.stations = yellow
        elif color == 'green':
            self.stations = green
        elif color == 'blue':
            self.stations = blue

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

    def move_trains(self):
        for train in self.trains:
            self.trains[train].move()

        for train in self.trains:
            for station in self.stations:
                if station.get_position() == train.get_position():
                    passengers_to_enter = station.get_persons()
                    people_boarded, report = train.open_doors(station, passengers_to_enter)
                    station.remove_persons_until_index(people_boarded)
                    self.report_satisfaction(report)
                    
    def update_line_info(self, hours, minutes, deliberations):
        for deliberation in deliberations:
            if re.match("train\d", deliberation):
                self.trains[deliberation].update_train_info(deliberations[deliberation])
            elif self.number_of_trains == deliberation:
                self.number_of_trains = deliberation

    def get_line_info(self):
        line_info = {}
        for train in self.trains:
            line_info[train] = self.trains[train].get_train_info()
        
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