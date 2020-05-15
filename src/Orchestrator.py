"""
Project by Artur Fortunato, João Coelho and Pedro Esteves.
"""
class Orchestrator:

    def __init__(self,new_lines):
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
    def percept(self,day_over,hours,minutes):
        self.hours = hours
        self.minutes = minutes

        for line in self.lines:
            self.perceptions[line.get_id()] = line.get_line_info()
        
            

    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    #Each invocation of this func deliberates  for a line taking in account the 4 line PERCEPTIONS
    #each line_perception is a dictionary the values of each train. the train ids are numerics.
    def choose_line_action(self, line_perception, line_color):
        res = {}
        res["trains"] = {}
        res['new_train'] = []
        #atualiza info relativo aos comboios
        for train_key in line_perception["trains"].keys():
            
            '''res["trains"][train_key]["position"] = {}
            res["trains"][train_key]["current_speed"] = line_perception["trains"][train_key]["current_speed"]
            res["trains"][train_key]["carriages"] = []
            res["trains"][train_key]["maximum_carriage"] = 3'''
            if(line_color == "blue"):#teste, brincadeira
                res["trains"][train_key] = {}
                res["trains"][train_key]["current_speed"] = line_perception["trains"][train_key]["current_speed"] + 4

        if not self.test_new_train and line_color == 'blue':
            res["new_train"] += [{'nr_carriages': 1,
                                  'speed': 2,
                                  'way': 1
                                }]
            self.test_new_train = True

        return res

    #nao passamos uma linha. Passamos percepcoes! do percept.
    def deliberate(self):
        for line_color in list(self.perceptions.keys()):
            self.deliberations[line_color] = self.choose_line_action(self.perceptions[line_color],line_color)    
        return self.deliberations
