from Orchestrator import Orchestrator
from Line import Line
from Reporter import Reporter

import Schedule_Getter as sg

import time

class Environment:

    def __init__(self):
        reporter = Reporter()
        self.lines = [ Line('red',2,[], reporter) , Line('yellow',2,[], reporter) , Line('blue',2,[], reporter) , Line('green',2,[], reporter) ]
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

    def move_trains(self):
        for line in self.lines:
            line.move_trains()
        
    def generatePeople(self):
        pass

    def run(self):
        while True:
            self.generatePeople()
            self.move_trains()
            self.orchestrator.percept(self.day_ended, self.hours, self.minutes)
            self.orchestrator.deliberate()
            self.orchestrator.actuate()
            self.tik()
            print("TIK")
            time.sleep(1)
