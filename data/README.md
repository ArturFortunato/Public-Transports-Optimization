# Dados

Este projeto foi realizado com dados reais do metro.

Para criar os modelos a partir dos dados:  

1- Correr parse_excels.py para gerar os csvs a partir dos excels originais.
2- Correr cleaner.py para gerar os csvs que vamos utilizar.
3 - Correr testes em ../src/Utils/Forecaster.py [Tem que se mudar os imports, tirar Util., para conseguir correr os testes]

Os modelos são gerados uma unica vez na inicialização de um forecaster, sendo guardados em Pickles:

## Pickles

models/final_station.pickle -> modelo que dada uma hora e uma estação inicial, devolve uma estação final.  

models/number_of_people.pickle -> modelo que dada uma hora e uma estação inicial, devolve o numero de pessoas que vão entrar nessa estação.  







