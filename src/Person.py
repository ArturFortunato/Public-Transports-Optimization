class Person:
    def __init__(self,pid, startingStation, finalStation):
        self.pId = pid
        self.startingStation = startingStation
        self.finalStation = finalStation
        self.waitingTime = 0
    
    #To be updated every tick the person is waiting
    def updateWaitingTime(self):
        self.waitingTime += 1

    def getStartingStation(self):
        return self.startingStation

    def getFinalStation(self):
            return self.finalStation