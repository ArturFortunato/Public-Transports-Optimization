class Person:
    def __init__(self,pid, starting_station, final_station, entered_time):
        self.pId = pid
        self.starting_station = starting_station
        self.final_station = final_station
        self.entered_time  = entered_time
    
    #To be updated every tick the person is waiting
    def get_entered_time(self):
        return self.entered_time

    def get_starting_station(self):
        return self.startingStation

    def get_final_station(self):
        return self.final_station