import pygame as pg

from Line import Line
import datetime

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0)
}

TRAIN_ID_OFFSET = [25, 12]

LINE_WIDTH = 2
STATION_COLOR = (255, 255, 255)
STATION_RADIUS = 5
TEXT_COLOR = (255, 255, 255)

class Gui:
    def __init__(self, env):
        pg.init()
        self.win = pg.display.set_mode((1500, 800))
        self.background = (0, 0, 0)
        self.trains = []
        self.lines = []
        self.stations = []
        self.reporter = None
        self.environment = env
    
    def run(self, day):
        if self.check_quit():
            return

        self.clear()
        self.draw(day)
        pg.display.update()

    def clear(self):
        self.win.fill(self.background)
    
    def draw_line(self, color, init_pos, end_pos):
        pg.draw.line(self.win, color, init_pos, end_pos, LINE_WIDTH)

    def draw_train(self, color, position, train_id, line):
        pg.draw.rect(self.win, color, position)
        self.write_train_id(position, train_id, line)

    def draw_station(self, position, name, text_position, nr_people, index=None):
        if position != None:
            pg.draw.circle(self.win, STATION_COLOR, position, STATION_RADIUS)
            if index == None:
                self.write_station_name(text_position, name, nr_people)
            else:
                self.write_station_name(text_position, name, nr_people, self.stations[index].get_people())

    def get_station_color(self, nr_people): #maybe change this for both ways?
        if nr_people[0] + nr_people[1] == 0:
            return (255, 255, 255)
        elif (nr_people[0] + nr_people[1]) / 2 <= 50:
            return (0, 255, 0)
        elif (nr_people[0] + nr_people[1]) / 2 <= 100:
            return (255, 255, 0)
        else:
            return (255, 0, 0)
            
    def write_station_name(self, station_position, station_name, nr_people, nr_people_extra=None):
        large_text = pg.font.Font('freesansbold.ttf', 15)
        if nr_people_extra == None:
            text_surf = large_text.render(station_name + " " + str(nr_people), True, self.get_station_color(nr_people))
        else:
            text_surf = large_text.render(station_name + " " + str(nr_people) + " " + str(nr_people_extra), True, self.get_station_color(nr_people))
        text_rect = text_surf.get_rect()
        text_rect.center = (station_position[0], station_position[1] + 15)
        self.win.blit(text_surf, text_rect)

    def write_train_id(self, train_position, train_id, color):
        large_text = pg.font.Font('freesansbold.ttf', 15)
        text_surf = large_text.render(str(train_id), True, TEXT_COLOR)
        text_rect = text_surf.get_rect()
        text_rect.center = (train_position[0] + TRAIN_ID_OFFSET[0], train_position[1] + TRAIN_ID_OFFSET[1])
        self.win.blit(text_surf, text_rect)
    
    def write_reports(self):
        base_text = "Global average waiting time:"
        large_text = pg.font.Font('freesansbold.ttf', 15)
        time = self.environment.time
        text_surf = large_text.render(base_text + str(self.reporter.get_average(time)), True, TEXT_COLOR)
        text_rect = text_surf.get_rect()
        self.win.blit(text_surf, text_rect)
    
    def write_current_time(self, day):
        base_day = "Day: "
        base_time = "Time: "
        large_text = pg.font.Font('freesansbold.ttf', 15)
        time = str(self.environment.time)
        text_surf = large_text.render(base_day + str(day) + " | " + base_time + time, True, TEXT_COLOR)
        text_rect = text_surf.get_rect()
        text_rect.center = (80, 33)
        self.win.blit(text_surf, text_rect)

    def draw(self, day):
        for i in range(len(self.lines)):
            self.draw_line(colors[self.lines[i].get_color()], self.lines[i].init_pos(), self.lines[i].end_pos())
        
        for i in range(len(self.stations)):
            if self.stations[i].get_draw():
                index = self.is_crossing(self.stations[i], i)
                if index == None:
                    self.draw_station(self.stations[i].get_gui_center(), self.stations[i].get_name(), self.stations[i].get_text_position(), self.stations[i].get_people())
                else:
                    self.draw_station(self.stations[i].get_gui_center(), self.stations[i].get_name(), self.stations[i].get_text_position(), self.stations[i].get_people(), index)
        
        for i in range(len(self.trains)):
            self.draw_train(self.trains[i].get_color(), self.trains[i].get_gui_position(), self.trains[i].get_id(), self.trains[i].get_line())
        
        self.write_reports()
        self.write_current_time(day)

    def is_crossing(self, current_station, index):
        for i in range(len(self.stations)):
            if self.stations[i].get_name() == current_station.get_name() and i != index:
                return i
        return None

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
    
    def delete_train(self, train_to_remove):
        for i in range(len(self.trains)):
            if self.trains[i].get_color() == train_to_remove.get_color() and self.trains[i].get_id() == train_to_remove.get_id():
                del self.trains[i]
                break