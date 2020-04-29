class Carriage:
    def __init__(self, maximum_capacity, taken_spots):
        self.maximum_capacity = maximum_capacity
        self.taken_spots = 0
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

    def remove_passengers(self, station):
        self.passengers = [passenger for passenger in self.passengers if passenger.get_final_station() != station]
        self.update_taken_spots()