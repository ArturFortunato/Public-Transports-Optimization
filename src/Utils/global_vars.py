import re
#Flags passadas pelo utilizador como input.
flags = {}

'''
Ex:
    lines=ALL
    lines=red
    lines=green
    lines=blue
    lines=yellow
'''
def add_flags(args):

    # Adiciona linhas

    re1 = re.compile('--lines=+')
    re2 = re.compile('--behavior=+')
    re3 = re.compile('--opt=+')
    flags['opt'] = None
    flags['colors'] = ['blue','green','red','yellow']
    flags['behavior'] = 'baseline'
    flags['std'] = False

    for arg in args:
        if re1.match(arg) != None:
            arg = arg.split('=')[1]
            if arg in ['blue','green','red','yellow']:
                flags['colors'] = [arg]
            elif arg == 'ALL':
                flags['colors'] = ['blue','green','red','yellow']
        if re2.match(arg) != None:
            arg = arg.split('=')[1]
            if arg in ['reactive', 'deliberative','baseline']:
                flags['behavior'] = arg
        if re3.match(arg) != None:
            arg = arg.split('=')[1]
            if arg in ['smooth', 'avg']:
                flags['opt'] = arg

    # Adiciona o envelope com o desvio padrao
    if '--std' in args: 
        flags['std'] = True
        
##### Auxiliar
RED = ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião']
BLUE = ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia']
YELLOW = ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato']
GREEN = ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']

stations_per_line = {
    "red": RED,
    "blue": BLUE,
    "yellow": YELLOW,
    "green": GREEN
}

stations = ['aeroporto', 'alameda', 'alfornelos', 'alto dos moinhos', 'alvalade', 'amadora este', 'ameixoeira', 'anjos', 'areeiro', 'avenida', 'baixa chiado', 'bela vista', 'cabo ruivo', 'cais do sodré', 'campo grande', 'campo pequeno', 'carnide', 'chelas', 'cidade universitária', 'colégio militar', 'encarnaçao', 'entre campos', 'intendente', 'jardim zoológico', 'laranjeiras', 'lumiar', 'marquês de pombal', 'martim moniz', 'moscavide', 'odivelas', 'olaias', 'olivais', 'oriente', 'parque', 'picoas', 'pontinha', 'praça de espanha', 'quinta das conchas', 'rato', 'reboleira', 'restauradores', 'roma', 'rossio', 'saldanha', 'santa apolónia', 'sao sebastiao', 'senhor roubado', 'telheiras', 'terreiro paço']

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

base_carriage_capacity = 185