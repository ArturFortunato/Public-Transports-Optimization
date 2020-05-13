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

    #Iterates the line list and extracts perceptions for each line.
        #dayOver - Boolean. It is true if the day is over, false if not.
        #hours - Received from the environment. The orchestrator
        #minutes - Received from the environment.
    def percept(self,day_over,hours,minutes):
        self.hours = hours
        self.minutes = minutes

        for line in self.lines:
            self.perceptions[line.get_id()] = line.get_line_info()
            
        #print(self.perceptions)


    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    #Each invocation of this func deliberates  for a line taking in account the 4 line PERCEPTIONS
    #each line_perception is a dictionary the values of each train. the train ids are numerics.
    def choose_line_action(self, line_perception):

        print("o valor da line_perception e: " + str(line_perception))
    
        pass

    #nao passamos uma linha. Passamos percepcoes! do percept.
    def deliberate(self):
        for line_color in list(self.perceptions.keys()):
            self.deliberations[line_color] = self.choose_line_action(self.perceptions[line_color])    

    def actuate(self):
        for line in self.lines:
            line.update_line_info(self.hours, self.minutes, self.deliberations)
        
        self.perceptions = {}
        self.deliberations = {}
        print("acabei de actuar")
        exit()


    def print_lines(self):
        print(self.lines)


