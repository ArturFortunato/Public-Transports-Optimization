class Station:
    def __init__(self, name, terminal_one, terminal_two, position, gui_center, text_offset, color, draw=True):
        self.name = name
        self.persons = {terminal_one: [], terminal_two: []}
        self.terminal_one = terminal_one
        self.terminal_two = terminal_two
        self.ways = {self.terminal_one: -1 , self.terminal_two: 1   }


        self.people_terminal_one = 0  #nr de pessoas no sentido negativo: t2 -> t1
        self.people_terminal_two = 0 #nr de pessoas no sentido positivo: t1 -> t2
        self.position = position
        self.gui_center = gui_center
        self.text_offset = text_offset
        self.draw = draw
        self.color = color 
        
    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
    
    def get_persons(self, way):
        return self.persons[self.terminal_two if way == 1 else self.terminal_one]

    def get_ways(self):
        return self.ways

    def get_gui_center(self):
        return self.gui_center

    def get_text_position(self): #change this to avoid overlap text and lines
        return [self.gui_center[0] + self.text_offset[0],
                self.gui_center[1] + self.text_offset[1]] 

    def get_people(self): #update for each sentido
        return (self.people_terminal_two, self.people_terminal_one)

    def get_draw(self):
        return self.draw

    def get_color(self):
        return self.color

    def add_person(self, person):
        self.persons[self.terminal_two if person.get_way() == 1 else self.terminal_one] += [person]
        if person.get_way() == 1: 
             self.people_terminal_two += 1
        else:
            self.people_terminal_one += 1

    def set_gui(self, gui):
        self.gui = gui
        gui.add_station(self)

    def remove_persons_until_index(self, idx, way):
        if way == 1:
            self.people_terminal_two -= idx           #subtrai o numero de pessoas em cada estacao
            terminal_station = self.terminal_two     #converte o sentido no terminal da estacao
        else:
            self.people_terminal_one -= idx           #subtrai o numero de pessoas em cada estacao
            terminal_station = self.terminal_one     #converte o sentido no terminal da estacao

        self.persons[terminal_station] = self.persons[terminal_station][idx:]

    def reset(self):
        self.persons = {self.terminal_one: [], self.terminal_two: []}
        self.people_terminal_one = 0 
        self.people_terminal_two = 0