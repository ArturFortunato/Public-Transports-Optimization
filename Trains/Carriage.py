class Carriage:
    def __init__(self, maximum_capacity, taken_spots):
        self.maximum_capacity = maximum_capacity
        self.taken_spots = 0

    def getCapacity(self):
        return self.maximum_capacity

    def updateTakenSpots(self, delta):
        self.taken_spots += delta