
from Station import Station

import re

#verde
telheiras = Station('telheiras', 'telheiras', 'cais_do_sodre', 0)
campo_grande = Station('campo_grande', 'telheiras', 'cais_do_sodre', 8)
alvalade = Station('alvalade', 'telheiras', 'cais_do_sodre', 20)
roma = Station('roma', 'telheiras', 'cais_do_sodre', 26)
areeiro = Station('areeiro', 'telheiras', 'cais_do_sodre', 33)
alameda = Station('alameda', 'telheiras', 'cais_do_sodre', 40)
arroios = Station('arroios', 'telheiras', 'cais_do_sodre', 44)
anjos = Station('anjos', 'telheiras', 'cais_do_sodre', 48)
intendente = Station('intendente', 'telheiras', 'cais_do_sodre', 53)
martim_moniz = Station('martim_moniz', 'telheiras', 'cais_do_sodre', 60)
rossio = Station('rossio', 'telheiras', 'cais_do_sodre', 65)
baixa_chiado = Station('baixa_chiado', 'telheiras', 'cais_do_sodre', 71)
cais_do_sodre = Station('cais_do_sodre', 'telheiras', 'cais_do_sodre', 78)

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, arroios, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('odivelas', 'odivelas', 'rato', 0)
senhor_roubado = Station('senhor_roubado', 'odivelas', 'rato', 4)
ameixoeira = Station('ameixoeira', 'odivelas', 'rato', 10)
lumiar = Station('lumiar', 'odivelas', 'rato', 18)
quinta_conchas = Station('quinta_conchas', 'odivelas', 'rato', 22)
campo_grande = Station('campo_grande', 'odivelas', 'rato', 31)
cidade_universitaria = Station('cidade_universitaria', 'odivelas', 'rato', 37)
entrecampos = Station('entrecampos', 'odivelas', 'rato', 41)
campo_pequeno = Station('campo_pequeno', 'odivelas', 'rato', 43)
saldanha = Station('saldanha', 'odivelas', 'rato', 51)
picoas = Station('picoas', 'odivelas', 'rato', 56)
marques_pombal = Station('marques_pombal', 'odivelas', 'rato', 59)
rato = Station('rato', 'odivelas', 'rato', 68)

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]


#vermelha
aeroporto = Station('aeroporto', 'aeroporto', 'sao_sebastiao', 0)
encarnacao = Station('encarnacao', 'aeroporto', 'sao_sebastiao', 7)
moscavide = Station('moscavide', 'aeroporto', 'sao_sebastiao', 12)
oriente = Station('oriente', 'aeroporto', 'sao_sebastiao', 20)
cabo_ruivo = Station('cabo_ruivo', 'aeroporto', 'sao_sebastiao', 24)
olivais = Station('olivais', 'aeroporto', 'sao_sebastiao', 29)
chelas = Station('chelas', 'aeroporto', 'sao_sebastiao', 36)
bela_vista = Station('bela_vista', 'aeroporto', 'sao_sebastiao', 41)
olaias = Station('olaias', 'aeroporto', 'sao_sebastiao', 48)
alameda = Station('alameda', 'aeroporto', 'sao_sebastiao',52)
saldanha = Station('saldanha', 'aeroporto', 'sao_sebastiao', 59)
sao_sebastiao = Station('sao_sebastiao', 'aeroporto', 'sao_sebastiao', 70)

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, alameda, saldanha, sao_sebastiao]

#azul
amadora_este = Station('amadora_este', 'amadora_este', 'santa_apolonia', 0)
alfornelos = Station('alfornelos', 'amadora_este', 'santa_apolonia', 7)
pontinha = Station('pontinha', 'amadora_este', 'santa_apolonia', 16)
carnide = Station('carnide', 'amadora_este', 'santa_apolonia', 21)
colegio_militar = Station('colegio_militar', 'amadora_este', 'santa_apolonia', 31)
alto_moinhos = Station('alto_moinhos', 'amadora_este', 'santa_apolonia', 36)
laranjeiras = Station('laranjeiras', 'amadora_este', 'santa_apolonia', 44)
jardim_zoologico = Station('jardim_zoologico', 'amadora_este', 'santa_apolonia', 49)
praca_espanha = Station('praca_espanha', 'amadora_este', 'santa_apolonia', 58)
sao_sebastiao = Station('sao_sebastiao', 'amadora_este', 'santa_apolonia', 68)
parque = Station('parque', 'amadora_este', 'santa_apolonia', 72)
marques_pombal = Station('marques_pombal', 'amadora_este', 'santa_apolonia', 77)
avenida = Station('avenida', 'amadora_este', 'santa_apolonia', 79)
restauradores = Station('restauradores', 'amadora_este', 'santa_apolonia', 82)
baixa_chiado = Station('baixa_chiado', 'amadora_este', 'santa_apolonia', 87)
terreio_paço = Station('terreio_paço', 'amadora_este', 'santa_apolonia', 91)
santa_apolonia = Station('amadora_este', 'amadora_este', 'santa_apolonia', 98)

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
        







    