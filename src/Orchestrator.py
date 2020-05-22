"""
Project by Artur Fortunato, João Coelho and Pedro Esteves.
"""
from Utils.global_vars import flags

class Orchestrator:

    def __init__(self, new_lines):
        self.lines = new_lines       #List that contains the metropolitan lines.
        self.perceptions = {}         #Perceptions list
        self.deliberations = {}
        self.hours = None
        self.minutes = None
        self.test_new_train = False

    #Iterates the line list and extracts perceptions for each line.
        #dayOver - Boolean. It is true if the day is over, false if not.
        #hours - Received from the environment. The orchestrator
        #minutes - Received from the environment.
    def percept(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

        for line in self.lines:
            self.perceptions[line.get_id()] = line.get_line_info()
        

    #receives as argument the way where the line is changing.
    def add_new_train(self, sentido):
        return [{'nr_carriages': 1, 'speed': 2, 'way': sentido}]

    
    def launch_trains(self,minutes,res,stations):
        if(flags["behavior"] == "baseline"):
            if self.minutes % 8 == 0 and self.minutes % 16 == 0:
                res['new_train'] += self.add_new_train(-1)

            #launch new train each 18 minutes
            elif self.minutes % 8 == 0:
                res['new_train'] += self.add_new_train(1)

        elif(flags["behavior"] == "reactive"):
            ways = stations[0].get_ways()
            for way in list(ways.keys()):
                n_persons = 0
                for station in stations: #itera todas as estacoes num sentido
                    n_persons += len(station.persons[way])

                if n_persons / len(stations) > 30:
                    res['new_train'] += self.add_new_train(ways[way])

            '''
            for station in stations:
                ways = station.get_ways()
                for key in list(ways.keys()): #key e uma estacao consoante o sentido
                    persons += len(station)
                    for person in station.persons[key]: #itera as pessoas da estacao num sentido
                        print(person)
                        exit()
            '''
        
        return res


    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    #Each invocation of this func deliberates  for a line taking in account the 4 line PERCEPTIONS
    #each line_perception is a dictionary the values of each train. the train ids are numerics.
    def choose_line_action(self, line_perception, line_color):
        res = {}
        res["trains"] = {}
        res['new_train'] = []

        #print(line_perception["trains"])
        #exit()

        if "stations" in  list(line_perception.keys()):
            res = self.launch_trains(self.minutes,res,line_perception["stations"])
        
        #atualiza info relativo aos comboios
        for train_key in line_perception["trains"].keys():
            
            '''res["trains"][train_key]["position"] = {}
            res["trains"][train_key]["current_speed"] = line_perception["trains"][train_key]["current_speed"]
            res["trains"][train_key]["carriages"] = []
            res["trains"][train_key]["maximum_carriage"] = 3'''
            if line_color == "blue":#teste, brincadeira
                res["trains"][train_key] = {}
                res["trains"][train_key]["current_speed"] = line_perception["trains"][train_key]["current_speed"] + 4

        if not self.test_new_train and line_color == 'blue':
            res["new_train"] += [{'nr_carriages': 1, 'speed': 2, 'way': 1}]
            self.test_new_train = True

        return res

    #nao passamos uma linha. Passamos percepcoes! do percept.
    def deliberate(self):
        for line_color in list(self.perceptions.keys()):
            self.deliberations[line_color] = self.choose_line_action(self.perceptions[line_color], line_color)    
        return self.deliberations
