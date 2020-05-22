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

    #Adiciona linhas
    re1 = re.compile('--lines=+')
    re2 = re.compile('--behavior=+')
    re3 = re.compile('--opt=+')
    flags["opt"] = None
    flags["colors"] = []
    flags["behavior"] = "baseline"
    flags["std"] = False

    for arg in args:
        if re1.match(arg) != None:
            arg = arg.split("=")[1]
            print(arg)
            if arg in ["yellow","green","blue","red"]:
                flags["colors"] = [arg]
            elif arg == "ALL":
                flags["colors"] = ["yellow","green","blue","red"]
        if re2.match(arg) != None:
            arg = arg.split("=")[1]
            if arg in ["reactive","deliberative"]:
                flags["behavior"] = arg
        if re3.match(arg) != None:
            arg = arg.split("=")[1]
            if arg in ["smooth","avg"]: flags["opt"] = arg

    #Adiciona o envelope com o desvio padrao
    if "--std" in args: flags["std"] = True

    



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
