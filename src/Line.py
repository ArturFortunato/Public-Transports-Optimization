
from Station import Station

#verde
telheiras = Station('telheiras', 'telheiras', 'cais_do_sodre')
campo_grande = Station('campo_grande', 'telheiras', 'cais_do_sodre')
alvalade = Station('alvalade', 'telheiras', 'cais_do_sodre')
roma = Station('roma', 'telheiras', 'cais_do_sodre')
areeiro = Station('areeiro', 'telheiras', 'cais_do_sodre')
alameda = Station('alameda', 'telheiras', 'cais_do_sodre')
arroios = Station('arroios', 'telheiras', 'cais_do_sodre')
anjos = Station('anjos', 'telheiras', 'cais_do_sodre')
intendente = Station('intendente', 'telheiras', 'cais_do_sodre')
martim_moniz = Station('martim_moniz', 'telheiras', 'cais_do_sodre')
rossio = Station('rossio', 'telheiras', 'cais_do_sodre')
baixa_chiado = Station('baixa_chiado', 'telheiras', 'cais_do_sodre')
cais_do_sodre = Station('cais_do_sodre', 'telheiras', 'cais_do_sodre')

green = [telheiras, campo_grande, alvalade, roma, areeiro, alameda, arroios, anjos, intendente, martim_moniz, rossio, baixa_chiado, cais_do_sodre]

#amarela
odivelas = Station('odivelas', 'odivelas', 'rato')
senhor_roubado = Station('senhor_roubado', 'odivelas', 'rato')
ameixoeira = Station('ameixoeira', 'odivelas', 'rato')
lumiar = Station('lumiar', 'odivelas', 'rato')
quinta_conchas = Station('quinta_conchas', 'odivelas', 'rato')
campo_grande = Station('campo_grande', 'odivelas', 'rato')
cidade_universitaria = Station('cidade_universitaria', 'odivelas', 'rato')
entrecampos = Station('entrecampos', 'odivelas', 'rato')
campo_pequeno = Station('campo_pequeno', 'odivelas', 'rato')
saldanha = Station('saldanha', 'odivelas', 'rato')
picoas = Station('picoas', 'odivelas', 'rato')
marques_pombal = Station('marques_pombal', 'odivelas', 'rato')
rato = Station('rato', 'odivelas', 'rato')

yellow = [odivelas, senhor_roubado, ameixoeira, lumiar, quinta_conchas, campo_grande, cidade_universitaria, entrecampos, campo_pequeno, saldanha, picoas, marques_pombal, rato]


#vermelha
aeroporto = Station('aeroporto', 'aeroporto', 'sao_sebastiao')
encarnacao = Station('encarnacao', 'aeroporto', 'sao_sebastiao')
moscavide = Station('moscavide', 'aeroporto', 'sao_sebastiao')
oriente = Station('oriente', 'aeroporto', 'sao_sebastiao')
cabo_ruivo = Station('cabo_ruivo', 'aeroporto', 'sao_sebastiao')
olivais = Station('olivais', 'aeroporto', 'sao_sebastiao')
chelas = Station('chelas', 'aeroporto', 'sao_sebastiao')
bela_vista = Station('bela_vista', 'aeroporto', 'sao_sebastiao')
olaias = Station('olaias', 'aeroporto', 'sao_sebastiao')
alameda = Station('alameda', 'aeroporto', 'sao_sebastiao')
saldanha = Station('saldanha', 'aeroporto', 'sao_sebastiao')
sao_sebastiao = Station('sao_sebastiao', 'aeroporto', 'sao_sebastiao')

red = [aeroporto, encarnacao, moscavide, oriente, cabo_ruivo, olivais, chelas, bela_vista, alameda, saldanha, sao_sebastiao]

#azul
amadora_este = Station('amadora_este', 'amadora_este', 'santa_apolonia')
alfornelos = Station('alfornelos', 'amadora_este', 'santa_apolonia')
pontinha = Station('pontinha', 'amadora_este', 'santa_apolonia')
carnide = Station('carnide', 'amadora_este', 'santa_apolonia')
colegio_militar = Station('colegio_militar', 'amadora_este', 'santa_apolonia')
alto_moinhos = Station('alto_moinhos', 'amadora_este', 'santa_apolonia')
laranjeiras = Station('laranjeiras', 'amadora_este', 'santa_apolonia')
jardim_zoologico = Station('jardim_zoologico', 'amadora_este', 'santa_apolonia')
praca_espanha = Station('praca_espanha', 'amadora_este', 'santa_apolonia')
sao_sebastiao = Station('sao_sebastiao', 'amadora_este', 'santa_apolonia')
parque = Station('parque', 'amadora_este', 'santa_apolonia')
marques_pombal = Station('marques_pombal', 'amadora_este', 'santa_apolonia')
avenida = Station('avenida', 'amadora_este', 'santa_apolonia')
restauradores = Station('restauradores', 'amadora_este', 'santa_apolonia')
baixa_chiado = Station('baixa_chiado', 'amadora_este', 'santa_apolonia')
terreio_paço = Station('terreio_paço', 'amadora_este', 'santa_apolonia')
santa_apolonia = Station('amadora_este', 'amadora_este', 'santa_apolonia')

blue = [amadora_este, alfornelos, pontinha, carnide, colegio_militar, alto_moinhos, laranjeiras, jardim_zoologico, praca_espanha, sao_sebastiao, parque, marques_pombal, avenida, restauradores, baixa_chiado, terreio_paço, santa_apolonia]



class Line:
    def __init__(self, color, maximum_trains, trains):
        self.color = color #string #considerated id
        self.maximum_trains = maximum_trains 
        self.trains = trains #dictionary of trains
        if color == 'red':
            self.stations = red
        elif color == 'yellow':
            self.stations = yellow
        elif color == 'green':
            self.stations = green
        elif color == 'blue':
            self.stations = blue

    def getId(self):
        return self.color

    def moveTrains(self):
        pass


    def updateLineInfo(self,hours,minutes):
        pass

    def getLineInfo(self):
        return 0

    def getTrainById(self, tid):
        return trains[tid]
        







    