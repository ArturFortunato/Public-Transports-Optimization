import Carriage

class Train:
    def __init__(self, tid, maximum_carriages, carriages, current_speed, maximum_speed, terminal_station, position):
        self.id = tid
        self.maximum_carriages = maximum_carriages
        self.carriages = carriages
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.terminal_station = self.terminal_station
        self.postion = position
    
    def change_speed(self, new_speed):
        if new_speed < maximum_speed:
            self.current_speed = new_speed
        else:
            self.current_speed = maximum_speed
    
    def get_train_info(self):
        train_info = {}
        train_info['position'] = self.postion
        train_info['current_speed'] = self.current_speed
        train_info['carriages'] = []
        train_info['maximum_carriage'] = self.maximum_carriages

        for carriage in self.carriages:
            train_info['carriages'] += [carriage.get_carriage_info()] 

        return train_info

    def move(self):
        self.postion += self.current_speed

    def open_doors(self, station, passengers):
        for carriage in self.carriages:
            carriage.remove_passengers(station)
            number_of_passengers_to_enter = min(carriage.current_capacity(), len(passengers))
            if number_of_passengers_to_enter != 0:
                carriage.add_passengers(passengers[:number_of_passengers_to_enter])
                passengers = passengers[number_of_passengers_to_enter:]
