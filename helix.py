# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:22:31 2021

@author: Edwin.Koch
"""

import numpy as np
import matplotlib.pyplot as plt

# helix parameters
r_h = 0.003
h = 0.001
c = 0
N = 5

# t vector for helix
t = np.linspace(0,N,100)

# helix calculations
x_x = r_h * np.cos(2*np.pi * t)
x_y = r_h * np.sin(2*np.pi * t)
x_z = h*t + c

x = [x_x, x_y, x_z]

# plane

#plane normal
n_p = [-1,0,0]
P = [0, 0, 0]
P_p =[1,1]
N_x = 10
N_y = 10



plt.close('all')
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
fig = plt.figure();
ax = plt.axes(projection='3d')
ax.plot(x_x, x_y, x_z)
