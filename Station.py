class Station:
    def __init__(self, name, terminalOne, terminalTwo):
        self.name = name
        self.terminalOne = terminalOne
        self.terminalTwo = terminalTwo
        self.peopleTerminalOne = 0
        self.peopleTerminalTwo = 0
        self.isTerminal = True if name == terminalOne or name == terminalTwo else False

    def setPeopleTerminalOne(self, n):
        self.peopleTerminalOne = n
    
    def setPeopleTerminalTwo(self, n):
        self.peopleTerminalTwo = n

    def updatePeopleTerminalOne(self, delta):
        self.peopleTerminalOne += delta

    def updatePeopleTerminalTwo(self, delta):
        self.peopleTerminalTwo += delta


    
