from Orchestrator import Orchestrator
from Line import Line

class Environment:

    def __init__(self):
        self.lines = [ Line('red',2,[]) , Line('yellow',2,[]) , Line('blue',2,[]) , Line('green',2,[]) ]
        self.orchestrator = Orchestrator(self.lines)
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

    def moveTrains(self):
        for line in self.lines:
            line.moveTrains()

    def run(self):
        while True:
            self.moveTrains()
            print("bacanao")
            print("-")
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            self.orchestrator.deliberate()
            self.orchestrator.actuate()
            self.tik()
