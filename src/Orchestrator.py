"""
Project by Artur Fortunato, João Coelho and Pedro Esteves.
"""
class Orchestrator:


    def __init__(self,new_lines):
        self.lines = new_lines       #List that contains the metropolitan lines.
        self.percepcoes = {}         #Perceptions list
        self.deliberacoes = {}
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
            self.percepcoes[line.getId()] = line.getLineInfo()



    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    def chooseLineAction(self,line):
        pass

    def deliberate(self):
        for line in self.lines:
            self.deliberacoes[line.getId()] = self.chooseLineAction(line)            

    def actuate(self):
        #self.hours = 12
        #self.minutes = 27
        for line in self.lines:
            line.updateLineInfo(self.hours,self.minutes)
        
        self.percepcoes = {}
        self.deliberacoes = {}



    def printLines(self):
        print(self.lines)


