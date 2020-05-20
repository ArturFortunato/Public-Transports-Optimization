

#Flags passadas pelo utilizador como input.
flags = {}
def add_flags(args):
    if "-v" in args: flags["verbose"] = True
    else: flags["verbose"] = False

##### Auxiliar

#rethink station and line design if this seems too ugly
red = ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião']
blue = ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia']
yellow = ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato']
green = ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
i = 0


#mudanca de linha
mudanca_linha = ["São Sebastião","Marquês de Pombal","Saldanha","Baixa Chiado","Alameda","Campo Grande"]

stations_per_line = {
    "red": ['Aeroporto', 'Encarnação', 'Moscavide', 'Oriente', 'Cabo Ruivo', 'Olivais', 'Chelas', 'Bela Vista', 'Olaias', 'Alameda', 'Saldanha', 'São Sebastião'],
    "blue": ['Amadora Este', 'Alfornelos', 'Pontinha', 'Carnide', 'Colégio Militar', 'Alto dos Moinhos', 'Laranjeiras', 'Jardim Zoológico', 'Praça Espanha', 'São Sebastião', 'Parque', 'Marquês de Pombal', 'Avenida', 'Restauradores', 'Baixa Chiado', 'Terreiro Paço', 'Santa Apolónia'],
    "yellow": ['Odivelas', 'Senhor Roubado', 'Ameixoeira', 'Lumiar', 'Quinta das Conchas', 'Campo Grande', 'Cidade Universitária', 'Entre Campos', 'Campo Pequeno', 'Saldanha', 'Picoas', 'Marquês de Pombal', 'Rato'],
    "green": ['Telheiras', 'Campo Grande', 'Alvalade', 'Roma', 'Areeiro', 'Alameda', 'Arroios', 'Anjos', 'Intendente', 'Martim Moniz', 'Rossio', 'Baixa Chiado', 'Cais do Sodré']
}