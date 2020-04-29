class Person:
    def __init__(self,pid, starting_station, final_station):
        self.pId = pid
        self.starting_station = starting_station
        self.final_station = final_station
        self.waiting_time = 0
    
    #To be updated every tick the person is waiting
    def update_waiting_time(self):
        self.waiting_time += 1

    def get_starting_station(self):
        return self.startingStation

    def get_final_station(self):
            return self.final_station