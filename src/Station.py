class Station:
    def __init__(self, name, terminalOne, terminalTwo, position, gui_center, text_offset, draw=True):
        self.name = name
        self.persons = []
        self.terminalOne = terminalOne
        self.terminalTwo = terminalTwo
        self.peopleTerminalOne = 0
        self.peopleTerminalTwo = 0
        self.isTerminal = (name == terminalOne or name == terminalTwo)
        self.position = position
        self.gui_center = gui_center
        self.text_offset = text_offset
        self.draw = draw

    def set_gui(self, gui):
        self.gui = gui
        gui.add_station(self)

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


    def get_gui_center(self):
        return self.gui_center

    def get_text_position(self): #change this to avoid overlap text and lines
        return [self.gui_center[0] + self.text_offset[0], self.gui_center[1] + self.text_offset[1]] 

    def to_draw(self):
        return self.draw