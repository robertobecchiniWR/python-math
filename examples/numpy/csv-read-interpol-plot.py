# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:28:03 2015

Python script for post-processing data stored in a csv file

@author: lunet
"""
# Importing all required libraries
import numpy as np
import matplotlib.pyplot as plt

# Get data from the csv file
data = np.genfromtxt('data.csv',dtype=float,delimiter=',',names=True)

# Getting the fields
times = data['Time']
pressures = data['Pressure']
velocities = data['Velocity']

# Interpoling data to suppress measurement error
polyDeg = 25
# getting the coefficient of the best polynomial fit
pressuresPolyCoeff = np.polyfit(times,pressures,polyDeg)
velocitiesPolyCoeff = np.polyfit(times,velocities,polyDeg)

# Constructing the polynomial with the coefficients
pressuresPoly=np.poly1d(pressuresPolyCoeff)
velocitiesPoly=np.poly1d(velocitiesPolyCoeff)

# Evaluate the polynomial at each time
pressuresInter = pressuresPoly(times)
velocitiesInter = velocitiesPoly(times)

# Plotting all data
plt.figure()
plt.subplot(211)
plt.plot(times,pressures,'b',label="Measurements")
plt.plot(times,pressuresInter,'r',label="Interpolation")
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Comparison between measured and interpolated fields')
plt.legend(loc=4)
plt.subplot(212)
plt.plot(times,velocities,'b',label="Measurements")
plt.plot(times,velocitiesInter,'r',label="Interpolation")
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend(loc=1)
plt.show()