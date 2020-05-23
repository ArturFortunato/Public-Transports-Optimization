from datetime import datetime, date

TRAIN_HEIGHT = 20

class Train:
    def __init__(self, tid, maximum_carriages, carriages, starting_speed, maximum_speed, color, gui, stations, way, line):
        self.id = tid
        self.maximum_carriages = maximum_carriages
        self.carriages = carriages
        self.maximum_speed = maximum_speed
        self.current_speed = starting_speed
        self.position = stations[0].get_position()
        self.last_station = stations[0]
        self.stations = stations
        self.color = color
        # 1 para sentido normal, -1 para sentido contrario
        self.way = way
        self.line = line

        #gui stuff
        self.size = 50 * len(carriages)
        self.gui_positions = [stations[0].get_gui_center()[0], stations[0].get_gui_center()[1], self.size, TRAIN_HEIGHT] #change the 50's for x and y for the train
        gui.add_train(self)
    
    def get_id(self):
        return self.id

    def get_gui_position(self):
        return self.gui_positions
    
    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color

    def get_line(self):
        return self.line

    def get_way(self):
        return self.way
    
    def get_train_info(self):
        train_info = {}
        train_info["way"] = self.get_way()
        train_info['position'] = self.position
        train_info['current_speed'] = self.current_speed
        train_info['carriages'] = self.carriages
        train_info['maximum_carriage'] = self.maximum_carriages

        #for carriage in self.carriages:
        #    train_info['carriages'] += [carriage.get_carriage_info()] 

        return train_info

    def change_speed(self, new_speed):
        if self.position == self.stations[-1].get_position():
            self.current_speed = 0
        elif new_speed <= self.maximum_speed and self.position + self.way * new_speed <= self.get_next_station().get_position() and self.line.can_update_train_speed(self, self.position, new_speed):
            self.current_speed = new_speed
        # Deveriamos acrescentar self.line.can_update_train_speed(self.tid, self.position, self.way * (self.get_next_station().get_position() - self.position))?
        elif new_speed <= self.maximum_speed:
            self.current_speed = self.way * (self.get_next_station().get_position() - self.position)
        else:
            self.current_speed = self.maximum_speed

    def get_vector_between(self, station1, station2):
        pos1 = station1.get_gui_center()
        pos2 = station2.get_gui_center()
        return [pos2[0] - pos1[0], pos2[1] - pos1[1]]
        
    def update_train_info(self, info):
        if 'current_speed' in info:
            self.change_speed(info['current_speed'])

    def in_a_station(self):
        for station in self.stations:
            if station.get_position() == self.position:
                return station
        return None

    def get_next_station(self):
        for station in self.stations:
            if (station.position > self.position and self.way == 1) or (station.position < self.position and self.way == -1):
                return station
        return None

    def move(self):
        if self.gui_positions[:2] == self.stations[-1].get_gui_center()[:2]: 
            return 

        next_station = self.get_next_station()
        self.position += self.way * min(self.current_speed, abs(next_station.get_position() - self.position))
        in_a_station = self.in_a_station()

        if in_a_station != None:
            self.gui_positions = in_a_station.get_gui_center() + [self.size, TRAIN_HEIGHT]
            self.last_station = in_a_station
        else:
            last_station_position = self.last_station.get_gui_center()
            #fracao entre estações percorrida
            mult = abs((self.position - self.last_station.get_position()) / (next_station.get_position() - self.last_station.get_position()))
            #vetor entre 2 estações
            vec = self.get_vector_between(self.last_station, next_station)
            #soma a gui position da ultima estação o quanto mexemos desde que lá chegamos
            self.gui_positions = [last_station_position[0] + vec[0] * mult, last_station_position[1] + vec[1] * mult, self.size, TRAIN_HEIGHT]

    #falta discriminar sentido de passageiros
    #ele ta a fazer slice dos passageiros, ele nao esta a discriminar os passageiros.
    #certificar se pessoal nos dois sentidos esta entrar no comboio.
    #problema da concorrencia dos comboios
    def open_doors(self, station, passengers, time):
        passengers_to_exchange = None
        original_length = len(passengers)
        report = []
        for carriage in self.carriages:
            passengers_to_exchange = carriage.remove_passengers(station)
            number_of_passengers_to_enter = min(carriage.current_capacity(), len(passengers)) #verifica quantidade de pessoas a entrar
            

            if number_of_passengers_to_enter != 0:
                for passenger in passengers[:number_of_passengers_to_enter]:
                    waiting_time = datetime.combine(date.min, time) - datetime.combine(date.min, passenger.get_entered_time())
                    report.append(waiting_time)
                    
                carriage.add_passengers(passengers[:number_of_passengers_to_enter])
                passengers = passengers[number_of_passengers_to_enter:]
        return original_length - len(passengers), passengers_to_exchange, report

    
