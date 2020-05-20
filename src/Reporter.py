
from global_vars import flags

class Reporter:
    def __init__(self, gui):
        self.total_waiting_times = []
        self.waiting_times_per_line = {}
        self.waiting_times_per_line["red"] = []
        self.waiting_times_per_line["green"] = []
        self.waiting_times_per_line["blue"] = []
        self.waiting_times_per_line["yellow"] = []
        self.gui = gui
        gui.add_reporter(self)


    def add_passengers_satisfaction(self, report,color):
        for r in report:
            self.waiting_times_per_line[color].append(r.seconds)    #analysis per line
            self.total_waiting_times.append(r.seconds)              #total analysis


    def get_average(self,time):
        print(time)
        if len(self.total_waiting_times) == 0:
            return None
        else:
            for key in list(self.waiting_times_per_line.keys()):
                if(flags["verbose"] == "ALL" or flags["verbose"] == key):
                    self.printIndividualLineMetrics(key)
            return sum(self.total_waiting_times)/len(self.total_waiting_times)

    def printIndividualLineMetrics(self,key):
        if( len(self.waiting_times_per_line[key]) != 0 ):
            print("Linha " +str(key) + " - "  + str( round(sum(self.waiting_times_per_line[key]) / len(self.waiting_times_per_line[key]),2) )  + "  Pessoas:" + str(len(self.waiting_times_per_line[key])) )


    def generate_charts(self):
        print("Gerando charts")
        pass