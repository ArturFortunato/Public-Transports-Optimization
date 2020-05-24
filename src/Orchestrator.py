'''
Project by Artur Fortunato, Joao Coelho and Pedro Esteves.
'''

from Utils.global_vars import flags

class Orchestrator:

    def __init__(self, new_lines):
        self.lines = new_lines       #List that contains the metropolitan lines.
        self.perceptions = {}         #Perceptions list
        self.deliberations = {}
        self.hours = None
        self.minutes = None
        self.day = None
        self.test_new_train = False

        #regista o numero de trains por linha
        self.trains_per_line = {}
        self.trains_per_line["red"] = {}
        self.trains_per_line["blue"] = {}
        self.trains_per_line["green"] = {}
        self.trains_per_line["yellow"] = {}
        for c in ["red","blue","green","yellow"]:
            self.trains_per_line[c]["-1"] = 0
            self.trains_per_line[c]["1"] = 0

        if(flags["behavior"] == "deliberative"):
            self.reset_stored_perceptions()
                

    def reset_stored_perceptions(self):
        self.stored_perceptions = {}
        for h in range(6,24):
            self.stored_perceptions[h] = {}
            for m in range(0,61):
                self.stored_perceptions[h][m] = {}
                for c in ["red","green","blue","yellow"]:
                    self.stored_perceptions[h][m][c] = {}
                    for s in ["-1","1"]:
                        self.stored_perceptions[h][m][c][s] = {}
                        for key in ["lt","occ","avg_p"]:
                            self.stored_perceptions[h][m][c][s][key] = ""


    #faz a media de hora para ocupacao das carruagens e numero de pessoas
    def hour_avg(self,string,hour,color,way):
        acc = 0

        if hour == 6: m = 15
        else: m = 0
        for m in range(m,60):
            #print("o valor de self.stored_perceptions[hour][m][color]" + str(self.stored_perceptions[hour][m][color]))
            #print("o valor de self.stored_perceptions[hour][m][color][way]" + str(self.stored_perceptions[hour][m][color][way]))
            #print("o valor de self.stored_perceptions[hour][m][color][string]" + str(self.stored_perceptions[hour][m][color][way][string]))

            
            acc += self.stored_perceptions[hour][m][color][way][string]
        return acc/60

    #conta o numero de comboios lancados
    def count_hour_lt(self,hour,color,way):
        try:
            count = 0
            for m in range(0,60):
                #print(self.stored_perceptions[hour][m][color][way]["lt"])
                if(self.stored_perceptions[hour][m][color][way]["lt"]):
                    count += 1
        except:
            print(self.stored_perceptions[hour][m][color][way])
        return count

    def plan_schedule(self):
        plan = {}
        for hour in self.stored_perceptions.keys():
            plan[hour] = {}
            for color in ["blue","yellow","green","red"]:
                plan[hour][color] = {}
                for way in ["-1","1"]:
                        
                    plan[hour][color][way] = None
                    avg_p = self.hour_avg("avg_p",hour,color,way)
                    avg_o = self.hour_avg("occ",hour,color,way)
                    hour_lt = self.count_hour_lt(hour,color,way)

                    if avg_p  > 15 and avg_o > 0.4:
                        hour_lt += 1
                    else: hour_lt -= 1
                        
                    if(hour_lt != 0): #no trains launched during that hour
                        freq  = round((60 / hour_lt),0)
                    else:
                        freq = 0

                    minutos_de_partida = []
                    m = 0
                    while(m < 60):
                        minutos_de_partida.append(m)
                        m += freq
                    plan[hour][color][way] =  minutos_de_partida

        return plan
            
    
    def reset(self):
        for c in ["red","blue","green","yellow"]:
            self.trains_per_line[c]["-1"] = 0
            self.trains_per_line[c]["1"] = 0
        if(flags["behavior"] == "deliberative"):
            self.plan = self.plan_schedule()
            self.reset_stored_perceptions()
       
    def get_trains_per_line(self):
        return self.trains_per_line

    #Iterates the line list and extracts perceptions for each line.
        #dayOver - Boolean. It is true if the day is over, false if not.
        #hours - Received from the environment. The orchestrator
        #minutes - Received from the environment.
    def percept(self,day, hours, minutes):
        self.day = day
        self.hours = hours
        self.minutes = minutes
        for line in self.lines:
            self.perceptions[line.get_id()] = line.get_line_info()
        

    #receives as argument the way where the line is changing.
    def add_new_train(self, sentido):
        return [{'nr_carriages': 1, 'speed': 2, 'way': sentido}]


    #Guarda informacao para planeamento do dia asseguir
    def store_info_deliberative(self,metrics,color):
        if(self.hours != 0):
            for way in list(metrics.keys()):
                way = str(way)
                self.stored_perceptions[self.hours][self.minutes][color][way]["lt"] = metrics[way]["lt"]
                self.stored_perceptions[self.hours][self.minutes][color][way]["occ"] = metrics[way]["occ"]
                self.stored_perceptions[self.hours][self.minutes][color][way]["avg_p"] = metrics[way]["avg_p"]
            



    def launch_trains_baseline(self,res,color):
        train_launched = False
        if self.minutes % 8 == 0 and self.minutes % 16 == 0:
            res['new_train'] += self.add_new_train(-1)
            train_launched = True
            self.trains_per_line[color]["-1"]+=1


        #launch new train each 8 minutes
        elif self.minutes % 8 == 0:
            res['new_train'] += self.add_new_train(1)
            train_launched = True
            self.trains_per_line[color]["1"]+=1

        return train_launched,res


    #Devolve a media de passageiros e a ocupacao das carruagens por linha por sentido
    def get_line_metrics(self,line_perception):
        resultado = {}
        stations = line_perception["stations"]
        ways = stations[0].get_ways()
        for way in list(ways.keys()):
            n_persons = 0
            for station in stations: 
                n_persons += len(station.persons[way])

            trains = line_perception["trains"]
            total_occupancy = 0
            total_occupancy_train_counter = 0
            for train_key in trains:
                if(trains[train_key]["way"] == station.ways[way]):
                    for carriage in trains[train_key]["carriages"]:
                        total_occupancy = carriage.get_occupancy_ratio()
                        total_occupancy_train_counter+=1

            if total_occupancy_train_counter > 0 : 
                occupancy_ratio = total_occupancy / total_occupancy_train_counter
            else: occupancy_ratio = 0

                
            resultado[str(ways[way])] = {}
            resultado[str(ways[way])]["avg_p"] = n_persons / len(stations)
            resultado[str(ways[way])]["occ"] = occupancy_ratio

        return resultado

    
    #Esta funcao e chamada a cada tik para os 2 sentidos de uma linha
    def launch_trains(self,minutes,res,line_perception,color):
        stations = line_perception["stations"]

        if(flags["behavior"] == "baseline"): 
           _, res  = self.launch_trains_baseline(res,color)

        elif(flags["behavior"] == "reactive"):
            ways = stations[0].get_ways()
            for way in list(ways.keys()):

                #CONTA AS PESSOAS EM CADA ESTACAO NUM SENTIDO NUMA DADA LINHA
                n_persons = 0
                for station in stations: 
                    n_persons += len(station.persons[way])

                #CONTA AS OCUPACOES DOS COMBOIOS NUM SENTIDO NUMA DADA LINHA
                trains = line_perception["trains"]

                correct_trains = dict()
                for train in trains:
                    if trains[train]['way'] == ways[way]:
                        correct_trains[train] = trains[train]
                trains = correct_trains

                total_occupancy = 0
                total_occupancy_train_counter = 0
                for train_key in trains:
                    if(trains[train_key]["way"] == station.ways[way]):
                        for carriage in trains[train_key]["carriages"]:
                            total_occupancy = carriage.get_occupancy_ratio()
                            total_occupancy_train_counter+=1

                if total_occupancy_train_counter > 0 : 
                    occupancy_ratio = total_occupancy / total_occupancy_train_counter
                else: occupancy_ratio = 0

                #o or e porque podem nao existir trains a circular dai a ocupacao ser 0.
                if (n_persons / len(stations) > 20 and occupancy_ratio > 0.5) or (n_persons / len(stations) > 15 and trains == {}):
                    res['new_train'] += self.add_new_train(ways[way])
                    self.trains_per_line[color][str(ways[way])]+=1


        elif(flags["behavior"]  == "deliberative"):
            if(self.day == 1):
                launched, res  = self.launch_trains_baseline(res,color)
                metrics = self.get_line_metrics(line_perception)
                
                for way_key in list(metrics.keys()):
                    if(launched == True):
                        way = res["new_train"][0]["way"]
                        metrics[way_key]["lt"] = True
                    else: metrics[way_key]["lt"] = False
            else: #deliberativo

                metrics = self.get_line_metrics(line_perception)
                try:
                    for way in ["-1","1"]:
                        metrics[way]["lt"] = False
                        launch_array = self.plan[self.hours][color][way]

                        if(self.minutes in launch_array):
                            res['new_train'] += self.add_new_train(int(way))
                            self.trains_per_line[color][way]+=1
                            metrics[way]["lt"] = True
                except:
                    print(self.hours)
                    print(color)
                    print(way)

            self.store_info_deliberative(metrics,color)

        return res




    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    #Each invocation of this func deliberates  for a line taking in account the 4 line PERCEPTIONS
    #each line_perception is a dictionary the values of each train. the train ids are numerics.
    def choose_line_action(self, line_perception, line_color):
        res = {}
        res["trains"] = {}
        res['new_train'] = []
        res = self.launch_trains(self.minutes,res,line_perception,line_color)
        return res

    #nao passamos uma linha. Passamos percepcoes! do percept.
    def deliberate(self):
        for line_color in list(self.perceptions.keys()):
            #print("deliberate" + str(line_color))
            self.deliberations[line_color] = self.choose_line_action(self.perceptions[line_color], line_color)    
        return self.deliberations
