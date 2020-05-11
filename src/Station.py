class Station:
    def __init__(self, name, terminalOne, terminalTwo, position):
        self.name = name
        self.persons = []
        self.terminalOne = terminalOne
        self.terminalTwo = terminalTwo
        self.peopleTerminalOne = 0
        self.peopleTerminalTwo = 0
        self.isTerminal = (name == terminalOne or name == terminalTwo)
        self.position = position

    def setPeopleTerminalOne(self, n):
        self.peopleTerminalOne = n

    def get_name(self):
        return self.name

    def addPersonById(self):
        pass

    def addPerson(self, person):
        #a list won't be good for removal, change for dict but check if it is not being used elsewhere.
        #also check add by id?
        self.persons.append(person)

    def removePersonById(self):
        pass

    def updatePersons(self):
        pass

    def get_persons(self):
        return self.persons
    

    #probably not necessary
    def setPeopleTerminalTwo(self, n):
        self.peopleTerminalTwo = n

    def updatePeopleTerminalOne(self, delta):
        self.peopleTerminalOne += delta

    def updatePeopleTerminalTwo(self, delta):
        self.peopleTerminalTwo += delta


    
