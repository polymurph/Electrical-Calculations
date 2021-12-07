# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:28:50 2021

@author: Edwin
"""

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

import numpy as np

f = 10000

omega = 2 * np.pi * f

print('f', f,'\t[Hz]')
print('omega', omega, '\t[rad/s]')

u = 1;

j_m = np.zeros((4,1))

u_m = [[u],[0],[0],[0]]

k = 1;

# network
R_1 = 1000
R_2 = 1000
R_3 = 1000
R_4 = 1000

L_1 = 10*10^(-6)
L_2 = 10*10^(-6)
L_3 = 10*10^(-6)
L_4 = 10*10^(-6)

M = k / (np.sqrt((L_1**2)))

print('j_m = ', j_m, '\t[A]')
print('u_m = ', u_m, '\t[V]')

jj = 1.j
mm = -omega * M * jj
jo = omega * jj

N = [[R_1 + jo*L_2, mm, mm, mm],
     [mm, R_2 + jo*L_2, mm, mm],
     [mm, mm, R_3 + jo*L_3,mm],
     [mm, mm, mm, R_4 + jo * L_4]]

invN = np.linalg.inv(N)

out = np.dot(invN, u_m)

out = np.abs(out)

print('N', N)
print('invN',invN)

print('out',out)
