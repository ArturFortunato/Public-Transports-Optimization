
from Station import Station

import re

#verde
telheiras = Station('Telheiras', 'Telheiras', 'Cais do Sodré', 0)
campo_grande = Station('Campo Grande', 'Telheiras', 'Cais do Sodré', 8)
alvalade = Station('Alvalade', 'Telheiras', 'Cais do Sodré', 20)
roma = Station('Roma', 'Telheiras', 'Cais do Sodré', 26)
areeiro = Station('Areeiro', 'Telheiras', 'Cais do Sodré', 33)
alameda = Station('Alameda', 'Telheiras', 'Cais do Sodré', 40)
arroios = Station('Arroios', 'Telheiras', 'Cais do Sodré', 44)
anjos = Station('Anjos', 'Telheiras', 'Cais do Sodré', 48)
intendente = Station('Intendente', 'Telheiras', 'Cais do Sodré', 53)
martim_moniz = Station('Martim Moniz', 'Telheiras', 'Cais do Sodré', 60)
rossio = Station('Rossio', 'Telheiras', 'Cais do Sodré', 65)
baixa_chiado = Station('Baixa Chiado', 'Telheiras', 'Cais do Sodré', 71)
cais_do_sodre = Station('Cais do Sodré', 'Telheiras', 'Cais do Sodré', 78)

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, arroios, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('Odivelas', 'Odivelas', 'Rato', 0)
senhor_roubado = Station('Senhor Roubado', 'Odivelas', 'Rato', 4)
ameixoeira = Station('Ameixoeira', 'Odivelas', 'Rato', 10)
lumiar = Station('Lumiar', 'Odivelas', 'Rato', 18)
quinta_conchas = Station('Quinta das Conchas', 'Odivelas', 'Rato', 22)
campo_grande = Station('Campo Grande', 'Odivelas', 'Rato', 31)
cidade_universitaria = Station('Cidade Universitária', 'Odivelas', 'Rato', 37)
entrecampos = Station('Entre Campos', 'Odivelas', 'Rato', 41)
campo_pequeno = Station('Campo Pequeno', 'Odivelas', 'Rato', 43)
saldanha = Station('Saldanha', 'Odivelas', 'Rato', 51)
picoas = Station('Picoas', 'Odivelas', 'Rato', 56)
marques_pombal = Station('Marquês de Pombal', 'Odivelas', 'Rato', 59)
rato = Station('Rato', 'Odivelas', 'Rato', 68)

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]


#vermelha
aeroporto = Station('Aeroporto', 'Aeroporto', 'São Sebastião', 0)
encarnacao = Station('Encarnação', 'Aeroporto', 'São Sebastião', 7)
moscavide = Station('Moscavide', 'Aeroporto', 'São Sebastião', 12)
oriente = Station('Oriente', 'Aeroporto', 'São Sebastião', 20)
cabo_ruivo = Station('Cabo Ruivo', 'Aeroporto', 'São Sebastião', 24)
olivais = Station('Olivais', 'Aeroporto', 'São Sebastião', 29)
chelas = Station('Chelas', 'Aeroporto', 'São Sebastião', 36)
bela_vista = Station('Bela Vista', 'Aeroporto', 'São Sebastião', 41)
olaias = Station('Olaias', 'Aeroporto', 'São Sebastião', 48)
alameda = Station('Alameda', 'Aeroporto', 'São Sebastião',52)
saldanha = Station('Saldanha', 'Aeroporto', 'São Sebastião', 59)
sao_sebastiao = Station('São Sebastião', 'Aeroporto', 'São Sebastião', 70)

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, alameda, saldanha, sao_sebastiao]

#azul
amadora_este = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 0)
alfornelos = Station('Alfornelos', 'Amadora Este', 'Santa Apolónia', 7)
pontinha = Station('Pontinha', 'Amadora Este', 'Santa Apolonia', 16)
carnide = Station('Carnide', 'Amadora Este', 'Santa Apolónia', 21)
colegio_militar = Station('Colégio Militar', 'Amadora Este', 'Santa Apolónia', 31)
alto_moinhos = Station('Alto dos Moinhos', 'Amadora Este', 'Santa Apolónia', 36)
laranjeiras = Station('Laranjeiras', 'Amadora Este', 'Santa Apolónia', 44)
jardim_zoologico = Station('Jardim Zoológico', 'Amadora Este', 'Santa Apolónia', 49)
praca_espanha = Station('Praça Espanha', 'Amadora Este', 'Santa Apolónia', 58)
sao_sebastiao = Station('São Sebastião', 'Amadora Este', 'Santa Apolónia', 68)
parque = Station('Parque', 'Amadora Este', 'Santa Apolónia', 72)
marques_pombal = Station('Marquês de Pombal 1', 'Amadora Este', 'Santa Apolónia', 77)
avenida = Station('Avenida', 'Amadora Este', 'Santa Apolónia', 79)
restauradores = Station('Restauradores', 'Amadora Este', 'Santa Apolónia', 82)
baixa_chiado = Station('Baixa Chiado', 'Amadora Este', 'Santa Apolónia', 87)
terreio_paço = Station('Terreiro Paço', 'Amadora Este', 'Santa Apolónia', 91)
santa_apolonia = Station('Amadora Este', 'Amadora Este', 'Santa Apolónia', 98)

blue = [amadora_este, alfornelos, pontinha, carnide, colegio_militar, alto_moinhos, laranjeiras, jardim_zoologico, praca_espanha, sao_sebastiao, parque, marques_pombal, avenida, restauradores, baixa_chiado, terreio_paço, santa_apolonia]



class Line:
    def __init__(self, color, maximum_trains, trains):
        self.color = color #string #considerated id
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
                    train.open_doors(station, []) #replace [] with list of new passengers

    def update_line_info(self,hours,minutes, deliberations):
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

    #need to change stations representations from list to dict, to avoid the for loop.
    def addPersonToStation(self, person, station):
        for s in self.stations:
            if s.name == station:
                s.addPerson(person)
        


    