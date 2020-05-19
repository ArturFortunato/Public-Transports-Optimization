class Station:
    def __init__(self, name, terminalOne, terminalTwo, position, gui_center, text_offset, draw=True):
        self.name = name
        self.persons = {terminalOne: [], terminalTwo: []}
        self.terminalOne = terminalOne
        self.terminalTwo = terminalTwo
        self.peopleTerminalOne = 0  #nr de pessoas no sentido negativo: t2 -> t1
        self.peopleTerminalTwo = 0 #nr de pessoas no sentido positivo: t1 -> t2
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

    def get_position(self):
        return self.position

    def addPersonById(self):
        pass

    def addPerson(self, person):
        self.persons[self.terminalTwo if person.get_way() == 1 else self.terminalOne] += [person]
        if person.get_way() == 1: 
             self.peopleTerminalTwo += 1
        else:
            self.peopleTerminalOne += 1

    def remove_persons_until_index(self, idx, way):
        if way == 1:
            self.peopleTerminalTwo -= idx           #subtrai o numero de pessoas em cada estacao
            terminal_station = self.terminalTwo     #converte o sentido no terminal da estacao
        else:
            self.peopleTerminalOne -= idx           #subtrai o numero de pessoas em cada estacao
            terminal_station = self.terminalOne     #converte o sentido no terminal da estacao

        self.persons[terminal_station] = self.persons[terminal_station][idx:]

    def removePersonById(self):
        pass

    def updatePersons(self):
        pass

    def get_persons(self, way):
        return self.persons[self.terminalTwo if way == 1 else self.terminalOne]
    

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

    def get_people(self): #update for each sentido
        return (self.peopleTerminalTwo, self.peopleTerminalOne)
    
    def get_terminal_1(self):
        return self.terminalOne

    def get_terminal_2(self):
        return self.terminalTwo