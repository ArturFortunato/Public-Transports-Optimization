# Public-Transports-Optimization
AASMA project repository

Projeto feito por: Artur Fortunato, João Coelho e Pedro Esteves.

Este projeto visa simular o metro de Lisboa utilizando dados do mês de Outubro de 2019.

Existem 3 modelos no projeto atualmente: baseline, reactive e deliberative.

É possível passar argumentos através do terminal para o programa. Estes argumentos incluem:

#How to run

python main.py

#FLAGS

--behavior : Esta flag controla o tipo de modelo a ser usado. Ela pode ter 3 valores. "reactive", "baseline" ou "deliberative".

--lines : Esta flag permite controlar as linhas plottadas. Pode ser "red", "green", "yellow", "blue" ou ALL

--opt : 
    Esta flag pode ter 2 valores:
        smooth - Faz sampling dos valores dos 2 gráficos (ocupação de carruagem e tempo médio de espera) de 15 em 15 minutos.
        avg - Pega nos valores dos últimos 15 minutos para o tempo médio de espera e ocupação de cada linha e calcula a média, fazendo smoothing ao gráfico.

--std : Adiciona um envelope aos plots com o desvio padrão.

Por omissão caso se corra apenas o projeto assim: "python main.py " O modo default é o baseline a plottar todas as linhas sem qualquer smoothing ou sampling.

#Exemplos

python main.py --lines=green (Plota apenas gráficos para a linha verde)

python main.py --lines=ALL (Plota gráficos para todas as linhas)

python main.py --lines=blue --std (Plota gráficos para a linha azul com o envelope do desvio padrão)

python main.py --lines=ALL --std --opt=smooth (Plota todos os gráficos com o envelope de std e desvio padrão)

python main.py --lines=ALL --std --opt=avg --behavior=reactive (Corre o modelo reactivo plottando todas as linhas com averaging a cada 15 minutes mais os envelopes de desvio padrao).