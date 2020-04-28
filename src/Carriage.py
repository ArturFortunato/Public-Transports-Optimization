class Carriage:
    def __init__(self, maximum_capacity, taken_spots):
        self.maximum_capacity = maximum_capacity
        self.taken_spots = 0

    def get_capacity(self):
        return self.maximum_capacity

    def update_taken_spots(self, delta):
        self.taken_spots += delta

    def get_carriage_info(self):
        carriage_info = {}
        
        carriage_info['maximum_capacity'] = self.maximum_capacity
        carriage_info['taken_spots'] = self.taken_spots

        return carriage_info
