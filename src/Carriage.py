class Carriage:
    def __init__(self, maximum_capacity, taken_spots=0):
        self.maximum_capacity = maximum_capacity
        self.taken_spots = taken_spots
        self.passengers = []

    def get_capacity(self):
        return self.maximum_capacity

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

    def printAlguemSaiu(self):
        print("alguem saiu")
        exit()

    def remove_passengers(self, station):
        passengers_left = []
        for passenger in self.passengers:
            #print( str(station.name) +  " - " + str(passenger.get_final_station()))
            if(passenger.get_final_station() != station.name):
                passengers_left.append(passenger)
        self.passengers = passengers_left            
        self.update_taken_spots()