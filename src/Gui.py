import pygame as pg

from Line import Line

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0)
}

LINE_WIDTH = 2
STATION_COLOR = (255, 255, 255)
STATION_RADIUS = 5

class Gui:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((1500, 800))
        self.background = (0,0,0)
        self.trains = []
        self.lines = []
        self.stations = []
        self.reporter = None
    
    def run(self):
        if self.check_quit():
            return

        self.clear()
        self.draw()
        pg.display.update()

    def clear(self):
        self.win.fill(self.background)
    
    def draw_line(self, color, init_pos, end_pos):
        pg.draw.line(self.win, color, init_pos, end_pos, LINE_WIDTH)

    def draw_train(self, color, position):
        pg.draw.rect(self.win, color, position)

    def draw_station(self, position, name, text_position, nr_people):
        if position != None:
            pg.draw.circle(self.win, STATION_COLOR, position, STATION_RADIUS)
            self.write_station_name(text_position, name, nr_people)

    def get_station_color(self, nr_people):
        if nr_people == 0:
            return (255,255,255)
        elif nr_people <= 5:
            return (0,255,0)
        elif nr_people <= 10:
            return (255,255,0)
        else:
            return (255,0,0)
            
    def write_station_name(self, station_position, station_name, nr_people):
        largeText = pg.font.Font('freesansbold.ttf', 15)
        textSurf = largeText.render(station_name + "(" + str(nr_people) + ")", True, self.get_station_color(nr_people))
        textRect = textSurf.get_rect()
        textRect.center = (station_position[0],station_position[1] + 15)
        self.win.blit(textSurf, textRect)

    def write_reports(self):
        base_text = "Global average waiting time:"
        largeText = pg.font.Font('freesansbold.ttf', 15)
        textSurf = largeText.render(base_text + str(self.reporter.get_average()), True, STATION_COLOR)
        textRect = textSurf.get_rect()
        self.win.blit(textSurf, textRect)

    def draw(self):
        for i in range(len(self.lines)):
            self.draw_line(colors[self.lines[i].get_color()], self.lines[i].init_pos(), self.lines[i].end_pos())
        for i in range(len(self.stations)):
            if self.stations[i].to_draw():
                self.draw_station(self.stations[i].get_gui_center(), self.stations[i].get_name(), self.stations[i].get_text_position(), self.stations[i].get_people())
        for i in range(len(self.trains)):
            self.draw_train(self.trains[i].get_color(), self.trains[i].get_gui_position())
        self.write_reports()

    def add_train(self, train):
        self.trains += [train]

    def add_line(self, line):
        self.lines += [line]

    def add_station(self, station):
        self.stations += [station]

    def add_reporter(self, reporter):
        self.reporter = reporter

    def check_quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                return True
        return False