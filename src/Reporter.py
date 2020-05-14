class Reporter:
    def __init__(self, gui):
        self.waiting_times = []
        self.gui = gui
        gui.add_reporter(self)


    def add_passengers_satisfaction(self, report):
        for r in report:
            self.waiting_times.append(r.seconds)

    def get_average(self):
        if len(self.waiting_times) == 0:
            return None
        else:
            return sum(self.waiting_times)/len(self.waiting_times)
