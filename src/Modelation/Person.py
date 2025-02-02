class Person:
    def __init__(self, starting_station, final_station, entered_time, positive_way):
        self.starting_station = starting_station
        self.final_station = final_station
        self.entered_time = entered_time
        self.positive_way = positive_way #if the person is travelling in positive way = T, else false. Positive is station.terminal1 -> sation.terminal2  
    
    def get_starting_station(self):
        return self.starting_station

    def get_final_station(self):
        return self.final_station

    def get_entered_time(self):
        return self.entered_time

    def get_way(self):
        return self.positive_way

    # se encontrar a estação de destino primeiro deve andar no sentido positivo, caso contrario anda no sentido negativo
    def update_way(self, line, current_station):
        for station in line.get_stations():
            if station.get_name() == current_station:
                self.positive_way = 1
                break
            elif station.get_name() == self.final_station:
                self.positive_way = -1
                break

    #Funcao que atualiza o tempo de entrada de uma pessoa numa nova estacao(troca de linha)
    def reset_entered_time(self, new_reset_time):
        self.entered_time = new_reset_time