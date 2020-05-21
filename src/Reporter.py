
from global_vars import flags
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

class Reporter:
    def __init__(self, gui):
        self.total_waiting_times = []
        self.waiting_times_per_line = {}

        #Apenas imprime no terminal.
        self.waiting_times_per_line["red"] = []
        self.waiting_times_per_line["green"] = []
        self.waiting_times_per_line["blue"] = []
        self.waiting_times_per_line["yellow"] = []

        #Guarda os resultados da funcao printIndividual LineMetrics
        self.avg_waiting_time_hour = {}
        for c in flags["verbose"]:
            self.avg_waiting_time_hour[c] = []
        
        #Guarda as horas.
        self.hours = []

        self.gui = gui
        gui.add_reporter(self)


    def add_passengers_satisfaction(self, report, color, time):
        for r in report:
            self.waiting_times_per_line[color].append(r.seconds)    #analysis per line
            self.total_waiting_times.append(r.seconds)              #total analysis


    def get_average(self, time):
        #print(time)
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

            print("Linha " +str(key) + " - "  + str(avg_waiting_time)  + "  Pessoas:" + str(len(self.waiting_times_per_line[key])) )


    def format_title_metro_colors(self):
        res = "("
        for c in range(0,len(flags["verbose"])):
            res += flags["verbose"][c]
            if(c != len(flags["verbose"])-1): res += ", "
            else: res += ")"
        return res

    def generate_charts(self):
        if(flags["verbose"] != []):
            self.plot_average_waiting_time()



    def plot_average_waiting_time(self):    
        fig, axs = plt.subplots(1)
        fig.suptitle('Daily Avg Waiting Time Per Line ' + self.format_title_metro_colors() + ":", fontsize=12)
        plt.xlabel('Time (HH:MM:SS)')
        plt.ylabel('Avg Waiting Time')
        for color in flags["verbose"]:

            y = self.avg_waiting_time_hour[color]
            x = self.hours
            size = min(len(y),len(x))
            # plot
            plt.plot(x[0:size], y[0:size],color)
            plt.gcf().autofmt_xdate()

        fig.savefig('../plots/daily_average_waiting_time.png')
        plt.show()


