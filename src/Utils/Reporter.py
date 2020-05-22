
from Utils.global_vars import flags
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
from os import path

class Reporter:
    def __init__(self, gui,day):
        self.day = day
        self.total_waiting_times = []
        self.waiting_times_per_line = {}

        #Apenas imprime no terminal.
        self.waiting_times_per_line["red"] = []
        self.waiting_times_per_line["green"] = []
        self.waiting_times_per_line["blue"] = []
        self.waiting_times_per_line["yellow"] = []

        #Guarda os resultados da funcao printIndividual LineMetrics
        self.avg_waiting_time_hour = {}

        #Guarda a ocupacao media de cada comboio
        self.avg_train_occupancy = {}

        for c in flags["verbose"]:
            self.avg_waiting_time_hour[c] = []
            self.avg_train_occupancy[c] = []
        #Guarda as horas.
        self.hours = []
        self.gui = gui
        gui.add_reporter(self)

    
    #faz reset dos parametros.
    def new_day_reset(self,show_plots):
        print("Reporter resetting...")
        self.day += 1

        #no início do primeiro dia não ha plots para mostrar
        if(self.day != 1): self.generate_charts(show_plots)
        
        self.hours = []

        for key in list(self.avg_train_occupancy.keys()):
            self.avg_waiting_time_hour[key] = []
            self.avg_train_occupancy[key] = []

        for key in list(self.waiting_times_per_line.keys()):
            self.waiting_times_per_line[key] = []



    def add_passengers_satisfaction(self, report, color, time):
        for r in report:
            self.waiting_times_per_line[color].append(r.seconds)    #analysis per line
            self.total_waiting_times.append(r.seconds)              #total analysis

    def report_average_train_occupancy(self,color,avg_train_occupancy):
        if color in flags["verbose"]:
            self.avg_train_occupancy[color].append(avg_train_occupancy)

    def get_average(self, time):
        if len(self.total_waiting_times) == 0:
            return None
        else:
            for key in list(self.waiting_times_per_line.keys()):
                if key in flags["verbose"]:
                    self.print_individual_line_metrics(key, time)
            return sum(self.total_waiting_times) / len(self.total_waiting_times)

    def print_individual_line_metrics(self, key, time):
        if( len(self.waiting_times_per_line[key]) != 0 ):
            avg_waiting_time = round(sum(self.waiting_times_per_line[key]) / len(self.waiting_times_per_line[key]), 2)

            #Importante para plottar.
            if(len(self.hours) == 0 or time != self.hours[-1]):
                self.hours.append(time)
            self.avg_waiting_time_hour[key].append(avg_waiting_time)  

            #print("Linha " +str(key) + " - "  + str(avg_waiting_time)  + "  Pessoas:" + str(len(self.waiting_times_per_line[key])) )


    def format_title_metro_colors(self):
        res = "("
        for c in range(0,len(flags["verbose"])):
            res += flags["verbose"][c]
            if(c != len(flags["verbose"])-1): res += ", "
            else: res += ") - Day " +  str(self.day)
        return res

    def generate_charts(self,show_plots):
        if(flags["verbose"] != []):
            self.plot_average_occupancy(show_plots)
            self.plot_average_waiting_time(show_plots)



    def plot_average_occupancy(self,show_plots):

        if path.exists('../plots/daily_average_occupancy_day' + str(self.day) + '.png'):
            os.remove('../plots/daily_average_occupancy_day'  + str(self.day) + '.png')

        fig = plt.figure()
        fig.suptitle('Daily Avg Occupancy Per Line ' + self.format_title_metro_colors() + ":", fontsize=12)
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Avg Occupancy')
        xformatter = matplotlib.dates.DateFormatter('%H:%M')
        for color in flags["verbose"]:

            y = self.avg_train_occupancy[color]
            x = self.hours
            nx = []
            for i in x:
                nx.append(datetime.datetime.combine(datetime.date.min, i))

            size = min(len(y),len(nx)) -1
            plt.plot(nx[0:size], y[0:size],color)
            #plt.gcf().autofmt_xdate()
            plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)

        print("o valor de self.hours e: " + str(self.hours))

        print("Showing daily average occupancy...")
        print("o valor de self.day e: " + str(self.day) + "o valor do show_plots e: " + str(show_plots))
        plt.savefig('../plots/daily_average_occupancy_day' + str(self.day)  + '.png')
        
        if show_plots: plt.show()

        plt.close(fig)
        print("Saved daily average occupancy...")




    def plot_average_waiting_time(self,show_plots):
        if(path.exists('../plots/daily_average_waiting_time_day' + str(self.day) +  '.png')):
            os.remove('../plots/daily_average_waiting_time_day'  + str(self.day) + '.png')

        fig = plt.figure()
        fig.suptitle('Daily Avg Waiting Time Per Line ' + self.format_title_metro_colors() + ":", fontsize=12)
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Avg Waiting Time')
        xformatter = matplotlib.dates.DateFormatter('%H:%M')
        for color in flags["verbose"]:

            y = self.avg_waiting_time_hour[color]
            x = self.hours
            nx = []
            for i in x:
                nx.append(datetime.datetime.combine(datetime.date.min, i))
            size = min(len(y),len(nx)) -1
            # plot
            plt.plot(nx[0:size], y[0:size],color)
            plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)

        print("Showing average waiting time...")

        plt.savefig('../plots/daily_average_waiting_time'  + str(self.day) + '.png')

        if show_plots: plt.show()
        plt.close(fig)


   

