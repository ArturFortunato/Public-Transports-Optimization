from global_vars import stations_per_line

class Carriage:
    def __init__(self, maximum_capacity, line):
        self.maximum_capacity = maximum_capacity
        self.taken_spots = 0
        self.passengers = []
        self.line = line

    def get_capacity(self):
        return self.maximum_capacity

    def get_occupancy_ratio(self):
        return  self.taken_spots / self.maximum_capacity 

    def current_capacity(self):
        return self.maximum_capacity - self.taken_spots
        
    def update_taken_spots(self):
        self.taken_spots = len(self.passengers)

    def get_carriage_info(self):
        carriage_info = {}
        
        carriage_info['maximum_capacity'] = self.maximum_capacity
        carriage_info['taken_spots'] = self.taken_spots

        return carriage_info
    
    def add_passengers(self, passengers):
        self.passengers += passengers
        self.update_taken_spots()

    def get_station_line(self, station):
        for line in stations_per_line:
            if station in stations_per_line[line]:
                return line

    def get_crossing_station(self, other_line):
        for station_name in stations_per_line[self.line.color]:
            if station_name in stations_per_line[other_line]:
                return station_name

    def remove_passengers(self, station):
        passengers_remaining = []
        passengers_to_exchange = []
        for passenger in self.passengers:

            #if the station is in a different line
            if not passenger.get_final_station() in stations_per_line[self.line.get_color()]:
                final_line = self.get_station_line(passenger.get_final_station())
                if station.get_name() == self.get_crossing_station(final_line):
                    passengers_to_exchange += [passenger]
                else:
                    passengers_remaining.append(passenger)
            # is not in his destiny yet
            elif passenger.get_final_station() != station.name:
                passengers_remaining.append(passenger)

        self.passengers = passengers_remaining
        self.update_taken_spots()
        return passengers_to_exchange