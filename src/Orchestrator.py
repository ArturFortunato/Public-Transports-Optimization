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
        print(self.perceptions)


    #AI algorithm to calculate the optimal values for each train velocity and number of carriages.
    def choose_line_action(self, line):
        pass

    def deliberate(self):
        for line in self.lines:
            self.deliberations[line.get_id()] = self.choose_line_action(line)            

    def actuate(self):
        for line in self.lines:
            line.update_line_info(self.hours, self.minutes, self.deliberations)
        
        self.perceptions = {}
        self.deliberations = {}

    def print_lines(self):
        print(self.lines)


