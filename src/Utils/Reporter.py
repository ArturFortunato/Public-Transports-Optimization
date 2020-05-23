
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

        for c in ['blue','green','red','yellow']:
            self.avg_waiting_time_hour[c] = []
            self.avg_train_occupancy[c] = []
        #Guarda as horas.
        self.hours = []
        self.gui = gui
        gui.add_reporter(self)

    if(path.exists('../logs/logs.txt')):
        os.remove('../logs/logs.txt')


    def register_new_trains(self,decisions):
        for color in list(decisions.keys()):
            for t in decisions[color]["new_train"]:
                self.trains_per_line[color][str(t['way'])] += 1

    def print_trains_of_the_day(self,trains_per_line):
        res = "     METROS LANÇADOS POR LINHA:"
        print(res)
        res =  "-------------------------------------------------------" + "\n" + res
        for color in ['blue','green','red','yellow']:
            tmp = "         " + str(color) + ":"
            for way in ["-1","1"]:
                tmp += " Sentido  " + str(way)  + " : " + str(trains_per_line[color][way]) + "     "  
                print(tmp)          
            res += "\n" + tmp 
            print(tmp)
        return res


    def add_to_logs(self,trains_of_the_day):
        with open("../logs/logs.txt", "a") as file_object:
            file_object.write("\n-------------------------------------------------------\n")

            tmp = "REPORT DO DIA " + str(self.day) + " :"
            print(tmp)
            file_object.write(tmp + "\n")
            tmp = "-------------------------------------------------------"
            file_object.write(tmp + "\n")
            print(tmp)
            tmp = "     TEMPO MÉDIO DE ESPERA(s) E OCUPAÇÃO POR LINHA:"
            file_object.write(tmp + "\n")
            print(tmp)
            for c in ["green","yellow","blue", "red"]:
                tmp = "         " + str(c) + " : " + str( round(sum(self.waiting_times_per_line[c]) / len(self.waiting_times_per_line[c]),0)) + " segundos  - " + str(round(sum(self.avg_train_occupancy[c]) / len(self.avg_train_occupancy[c]),4))
                print(tmp)
                file_object.write(tmp + "\n")
            print("-------------------------------------------------------")
            file_object.write(self.print_trains_of_the_day(trains_of_the_day))
            print("#######################################################")
    

    #faz reset dos parametros.
    def new_day_reset(self,show_plots,trains_of_the_day):
        self.add_to_logs(trains_of_the_day)
        print("Reporter resetting...")
        #no início do primeiro dia não ha plots para mostrar
        if(self.day >= 1): self.generate_charts(show_plots)
        
        self.day += 1
        self.hours = []

        for key in list(self.avg_train_occupancy.keys()):
            self.avg_waiting_time_hour[key] = []
            self.avg_train_occupancy[key] = []



    def add_passengers_satisfaction(self, report, color, time):
        for r in report:
            self.waiting_times_per_line[color].append(r.seconds)    #analysis per line
            self.total_waiting_times.append(r.seconds)              #total analysis

    def report_average_train_occupancy(self,color,avg_train_occupancy):
        if color in flags["colors"]:
            self.avg_train_occupancy[color].append(avg_train_occupancy)

    def get_average(self, time):
        if len(self.total_waiting_times) == 0:
            return None
        else:
            for key in list(self.waiting_times_per_line.keys()):
                if key in flags["colors"]:
                    self.print_individual_line_metrics(key, time)
            return sum(self.total_waiting_times) / len(self.total_waiting_times)

    def print_individual_line_metrics(self, key, time):
        if( len(self.waiting_times_per_line[key]) != 0 ):
            avg_waiting_time = round(sum(self.waiting_times_per_line[key]) / len(self.waiting_times_per_line[key]), 2)

            #Importante para plottar.
            if(len(self.hours) == 0 or time != self.hours[-1]):
                self.hours.append(time)
            self.avg_waiting_time_hour[key].append(avg_waiting_time)  


    def format_title_metro_colors(self):
        res = "("
        for c in range(0,len(flags["colors"])):
            res += flags["colors"][c]
            if(c != len(flags["colors"])-1): res += ", "
            else: res += ") - Day " +  str(self.day)
        return res

    def format_behavior(self,b):
        if(b == "baseline"): return "Baseline"
        if(b == "reactive"): return "Reactive"
        if(b == "deliberative"): return "Deliberative"


    def generate_charts(self,show_plots):
        if(flags["colors"] != [] and self.hours != []):
            self.plot_average_occupancy(show_plots)
            self.plot_average_waiting_time(show_plots)




    def plot_average_occupancy(self,show_plots):
        if path.exists('../plots/daily_average_occupancy_day' + str(self.day) + '.png'):
            os.remove('../plots/daily_average_occupancy_day'  + str(self.day) + '.png')

        fig = plt.figure()
        fig.suptitle(str(self.format_behavior(flags["behavior"]))  + ' - Avg Occupancy Per Line ' + self.format_title_metro_colors() , fontsize=12)
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Avg Occupancy')
        xformatter = matplotlib.dates.DateFormatter('%H:%M')
        for color in flags["colors"]:

            y = self.avg_train_occupancy[color]
            x = self.hours

            nx = []
            for i in x:
                nx.append(datetime.datetime.combine(datetime.date.min, i))

            size = min(len(y),len(nx)) -1

            x = nx[0:size]
            y= y[0:size]

            if(flags["opt"] != None): x,y = self.apply_options(flags["opt"],x,y)


            plt.plot(x, y,color) #plot

            if(flags["std"] == True):
                error = np.random.normal(0.1, 0.02, size=len(y))
                plt.fill_between(x, y-error,y+error, color=color,alpha=0.4)

            plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)


        print("Showing daily average occupancy...")
        print("o valor do dia e: " + str(self.day))
        plt.savefig('../plots/daily_average_occupancy_day' + str(self.day)  + '.png')
        
        if show_plots: plt.show()

        plt.close(fig)
        print("Saved daily average occupancy...")


    def apply_options(self,opt,x,y):
        if flags["opt"] == "smooth" :
            x = [x[i] for i in range(len(x)) if i % 15 == 0]
            y = [y[i] for i in range(len(y)) if i % 15 == 0]

        elif flags["opt"] == "avg":
            avg_time = 5
            avg_x = []
            avg_y = []
            for ind in range(0,len(y)):
                if ind == 0:
                    avg_y.append(y[0])
                    avg_x.append(x[ind])
                elif ind % avg_time == 0:
                    numerador = (sum(y[ind-avg_time:ind]))
                    denominador = len(y[ind-avg_time:ind])
                    avg_y.append(numerador/denominador) 
                    avg_x.append(x[ind])
        return avg_x, avg_y


    def plot_average_waiting_time(self,show_plots):
        if(path.exists('../plots/daily_average_waiting_time_day' + str(self.day) +  '.png')):
            os.remove('../plots/daily_average_waiting_time_day'  + str(self.day) + '.png')

        fig = plt.figure()
        fig.suptitle(str(self.format_behavior(flags["behavior"])) + self.format_title_metro_colors() + " - Avg waiting Time(s) per Line " + str(self.format_behavior(flags["behavior"])), fontsize=12)
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Avg Waiting Time')
        xformatter = matplotlib.dates.DateFormatter('%H:%M')
        for color in flags["colors"]:

            y = self.avg_waiting_time_hour[color]
            x = self.hours

            
            nx = []
            for i in x:
                nx.append(datetime.datetime.combine(datetime.date.min, i))
            size = min(len(y),len(nx)) -1

            x = nx[0:size]
            y = y[0:size]

            if(flags["opt"] != None): x,y = self.apply_options(flags["opt"],x,y)


            plt.plot(x, y,color) #plot

            if(flags["std"] == True):
                error = np.random.normal(0.1, 0.02, size=len(y))

                plt.fill_between(x, y-error,y+error, color=color,alpha=0.4)

            plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)

        print("Showing average waiting time...")

        plt.savefig('../plots/daily_average_waiting_time'  + str(self.day) + '.png')

        if show_plots: plt.show()
        plt.close(fig)


   

