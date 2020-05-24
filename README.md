# Public-Transports-Optimization
Projeto para a cadeira de AASMA, IST, MEIC, 2020.  

Autores: Artur Fortunato, João Coelho e Pedro Esteves.  

Este projeto visa simular o metro de Lisboa utilizando dados do mês de Outubro de 2019.  

Existem 3 modelos no projeto atualmente: baseline, reactive e deliberative.  

É possível passar argumentos através do terminal para o programa.  


## Organização
/data/  
- Modelos para geração de pessoas. Dados sensiveis logo não está tudo aqui.  /data/models tem os pickles dos modelos.  

/logs/
- Logs gerados durante a execução do programa. Inclui número de comboios em cada linha em cada sentido e ocupação média.  

/plots/
- Gráficos gerados durante a execução do programa. Dois gráficos por dia, um da evolução do tempo médio de espera, outro da evolução da capacidade média dos comboios.  

/src/
- Código base. Na raíz tem o código relativo aos agentes (Orchestrator.py e Line.py) e ao Ambiente. Tem também o main.  

/src/Modelation  
- Código para modelar o metro de Lisboa.  

/src/Utils  
- Contem código para a GUI, previsões temporais baseadas no modelo, GUI, um Reporter que guarda a evolução das métricas e variáveis globais.  


## How to run

From src/:  

python3 main.py

### FLAGS

--behavior : Esta flag controla o tipo de modelo a ser usado. Ela pode ter 3 valores. "reactive", "baseline" ou "deliberative".

--lines : Esta flag permite controlar as linhas plottadas. Pode ser "red", "green", "yellow", "blue" ou "ALL"  

--opt : 
    Esta flag pode ter 2 valores:
        smooth - Faz sampling dos valores dos 2 gráficos (ocupação de carruagem e tempo médio de espera) de 15 em 15 minutos.
        avg - Pega nos valores dos últimos 15 minutos para o tempo médio de espera e ocupação de cada linha e calcula a média, fazendo smoothing ao gráfico.

--std : Adiciona um envelope aos plots com o desvio padrão.

Por omissão caso se corra apenas o projeto assim: "python main.py " O modo default é o baseline a produzir o plot com todas as linhas sem qualquer smoothing ou sampling.

### Exemplos

python main.py --lines=green (Plota apenas gráficos para a linha verde)

python main.py --lines=ALL (Plota gráficos para todas as linhas)

python main.py --lines=blue --std (Plota gráficos para a linha azul com o envelope do desvio padrão)

python main.py --lines=ALL --std --opt=smooth (Plota todos os gráficos com o envelope de std e desvio padrão)

python main.py --lines=ALL --std --opt=avg --behavior=reactive (Corre o modelo reactivo plottando todas as linhas com averaging a cada 15 minutes mais os envelopes de desvio padrao).


## Parametros

Cada comportamento depende de alguns parametros para realizar as escolhas. Estes parametros estão explicados no relatório.
Os parametros que temos de momento na implementação são:

Reactive:
- Ocupância Média: 20%.  
- Média de Pessoas por estação: 20.  

Deliberativo:
- Horario Inicial: Comboios a cada 16 minutos.  
- Ocupância Média: 40%.
- Média de Pessoas por Estação: 20.

Variações nestes valores irão produzir resultados diferentes.

A baseline atual está a lançar um comboio a cada 8 minutos.

