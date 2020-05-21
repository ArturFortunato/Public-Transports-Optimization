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
    p = re.compile('lines=+')
    flags["verbose"] = None
    for arg in args:
        if p.match(arg) != None:
            arg = arg.split("=")[1]
            if arg in ["yellow","green","blue","red"]:
                flags["verbose"] = [arg]
            elif arg == "ALL":
                flags["verbose"] = ["yellow","green","blue","red"]
        else:
            flags["verbose"] = []


##### Auxiliar

#rethink station and line design if this seems too ugly
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
