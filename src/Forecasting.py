import numpy
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
import datetime
import random

#generating a random dataset
#import the normal datetime for this, not panda's
""" init = datetime.datetime(2020, 12 , 1, 6, 15)
with open("random_dataset.csv", "w") as f:
    f.write("time,number\n")
    while True:
        f.write(str(init) + "," + str(random.randint(10,50)) + "\n")
        init = init + datetime.timedelta(minutes=15) 
        if init.day == 31:
            break  """


#AUTOREGULARIZATION???

series = read_csv('../data/parsed_data/data_per_station_count/aeroporto.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)

model = ARIMA(series, order=(5,1,0)) #check the values for the model with the real dataset
model_fit = model.fit(disp=0)

#baricentro

#predict from x to y. x has to be in-sample timestamp
#output1 = model_fit.predict("2020-12-30 23:45:00", "2020-12-31 11:15:00")
#forecast the 1st out of sample result
""" output2 = model_fit.predict("", "2018-11-02 11:15:00")
print(output2)
 """

#also use this to check if values are ok
#print(model_fit.summary())
# plot residual errors
""" residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe()) """


#tslearn
#barycenter
#DTW

#prediction

    