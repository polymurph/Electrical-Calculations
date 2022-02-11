# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:11:15 2022

@author: Edwin.Koch
"""

import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt
import scipy.optimize as scio

def get_aircoil_windings(inductance,
                         winding_length,
                         radius):
    return np.sqrt(sc.mu_0 * radius**2 * np.pi / (inductance * winding_length))
    

def get_aircoil_inductance(windings,
                           radius,
                           length):
    return windings**2 * sc.mu_0 * radius**2 * np.pi/length

# coil body specs
coil_winding_length = 0.08
coil_body_diameter = 0.04

# wire specs
wire_diameter = 0.001
wire_resistance_per_length = 1

print(get_aircoil_windings(0.00003,0.035,0.02))


L_calc = get_aircoil_inductance(136,0.03,0.145)
L_meas = 0.003951


# https://www.amplifier.cd/Tutorial/Exponential%20Fit/Exponential%20Fit.html
dia_to_len = np.linspace(0, 40,40)


#• https://www.kite.com/python/answers/how-to-do-exponential-and-logarithmic-curve-fitting-in-python

x_data = [0.5,5.5,10,17,24,34]
y_data = [0.85,0.3,0.2,0.15,0.125,0.1]

# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
c = scio.curve_fit(lambda t,a,b: a*np.exp(b*t),  x_data,  y_data,  p0=(4, 0.1))
print(c)
a = 1.1#0.88268784
b = -0.25#-0.14938887
print("a = ",a)
print("b = " ,b)

k = a * np.exp( b* dia_to_len)

plt.plot(dia_to_len, k)
plt.plot(x_data,y_data)
plt.grid()
plt.show()


