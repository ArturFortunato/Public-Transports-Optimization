from Carriage import Carriage


from datetime import datetime, date
import time

TRAIN_HEIGHT = 20

class Train:
    def __init__(self, tid, maximum_carriages, carriages, current_speed, maximum_speed, terminal_station, position, color, gui, stations):
        self.id = tid
        self.maximum_carriages = maximum_carriages
        self.carriages = carriages
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.terminal_station = terminal_station
        self.position = position
        self.last_station = stations[0]
        self.stations = stations
        self.color = color
        
        #gui stuff
        self.size = 50 * len(carriages)
        self.gui_positions = [50, 50, self.size, TRAIN_HEIGHT] #change the 50's for x and y for the train
        gui.add_train(self)
    
    def get_next_station(self):
        for station in self.stations: #this will blow up whe train moving backwards
            if station.position >= self.position:
                return station

    def change_speed(self, new_speed):
        if new_speed < maximum_speed and self.position + new_speed <= self.get_next_station().get_position():
            self.current_speed = new_speed
        elif new_speed < maximum_speed:
            self.current_speed = self.get_next_station().get_position() - self.position
        else:
            self.current_speed = maximum_speed
    
    def get_train_info(self):
        train_info = {}
        train_info['position'] = self.position
        train_info['current_speed'] = self.current_speed
        train_info['carriages'] = []
        train_info['maximum_carriage'] = self.maximum_carriages

        #for carriage in self.carriages:
        #    train_info['carriages'] += [carriage.get_carriage_info()] 

        return train_info

    def get_vector_between(self, station1, station2):
        pos1 = station1.get_gui_center()
        pos2 = station2.get_gui_center()
        return [pos2[0] - pos1[0], pos2[1] - pos1[1]]

    def move(self):
        if self.position == self.stations[-1].get_position():
            return 

        self.position += self.current_speed
        next_station = self.get_next_station()
        if self.position == next_station.get_position():
            self.gui_positions = next_station.get_gui_center() + [self.size, TRAIN_HEIGHT]
            self.last_station = next_station
        else:
            last_station_position = self.last_station.get_gui_center()
            #fracao entre estações percorrida
            mult = (self.position - self.last_station.get_position()) / (next_station.get_position() - self.last_station.get_position())
            #vetor entre 2 estações
            vec = self.get_vector_between(self.last_station, next_station)
            #soma a gui position da ultima estação o quanto mexemos desde que lá chegamos
            self.gui_positions = [last_station_position[0] + vec[0] * mult, last_station_position[1] + vec[1] * mult, self.size, TRAIN_HEIGHT]

    def open_doors(self, station, passengers, time):
        original_length = len(passengers)
        report = []
        for carriage in self.carriages:
            carriage.remove_passengers(station)
            number_of_passengers_to_enter = min(carriage.current_capacity(), len(passengers))
            if number_of_passengers_to_enter != 0:
                for p in passengers[:number_of_passengers_to_enter]:
                    waiting_time = datetime.combine(date.min, time) - datetime.combine(date.min, p.get_entered_time()) 
                    report.append(waiting_time)
                carriage.add_passengers(passengers[:number_of_passengers_to_enter])
                passengers = passengers[number_of_passengers_to_enter:]
        print("entered" +  str(original_length - len(passengers)) + " at " + station.name)
        return original_length - len(passengers), report

    def get_gui_position(self):
        return self.gui_positions
    
    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color