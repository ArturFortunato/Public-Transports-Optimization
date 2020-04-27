import Trains.Carriage

class Train:
    def __init__(self, tid, maximum_carriages, carriages, current_speed, maximum_speed, terminal_station, position):
        self.id = tid
        self.maximum_carriages = maximum_carriages
        self.carriages = carriages
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.terminal_station = self.terminal_station
        self.postion = position

    
    def changeSpeed(self, new_speed):
        if new_speed < maximum_speed:
            self.current_speed = new_speed
        else:
            self.current_speed = maximum_speed




