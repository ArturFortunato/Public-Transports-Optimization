import Orchestrator
import Line

class Environment:

    self.orchestrator
    self.hours
    self.minutes
    self.day_ended

    def Environment(self):
        self.orchestrator = Orchestrator(self.create_lines())
        self.day_ended = False
        self.start_day()

    def start_day(self):
        self.hours = 6
        self.minutes = 0
    
    def tik(self):
        if self.minutes != 59:
            self.minutes += 1
        else:
            self.minutes = 0 
            self.hours = (self.hours + 1) % 24

            if self.hours == 1:
                self.day_ended = True
    
    def create_lines(self):
        return [ Line('red') , Line('yellow') , Line('blue') , Line('green') ]

    def run(self):
        while True:
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            self.orchestrator.actuate()
            self.tik()
