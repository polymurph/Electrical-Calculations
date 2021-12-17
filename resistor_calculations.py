# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:49:05 2021

@author: Edwin.Koch
"""

import numpy as np


R1 = 38000
R2 = 10000000

sR1 = 0.0001
sR2 = 0.0001


g = R2/R1

# gausssche fehlerfortpflanzung von R2/R2
sg = np.sqrt((-R2/(R1**2)*sR1)**2 + (1/R1*sR2)**2)

print('gain = ', g)
print('standart deviation of gain = ', sg)


V = 5

Vout = V*g
print(Vout)
delta_Vout = V*(g+sg) - V*(g-sg)
print(delta_Vout)



delta_T = 10


delta_R1 = sR1*10*R1
delta_R2 = sR2*10*R2

delta_g = (R2+delta_R2)/(R1+delta_R1)

print(delta_g)
print(g)

print(V*g - V* delta_g)

print('######################################################################')

# TCR influence calculations of inverted opamp amplifier cirquit
# https://passive-components.eu/understanding-high-precision-resistor-temperature-coefficient-of-resistance/

TCR_R1 = 0.000001 # 10ppm
TCR_R2 = 0.000001 # 10ppm

delta_T_R1 = 1.1
delta_T_R2 = 1

delta_R1 = TCR_R1 * R1 / delta_T_R1
delta_R2 = TCR_R2 * R2 / delta_T_R2

G_nt = - R2 / R1
G = - (delta_R2 + R2) / (delta_R1 + R1)


print(G_nt)
print(G)

U_in = 1

U_out_nt = G_nt * U_in
U_out = G * U_in

delta_U_out = U_out - U_out_nt
print(delta_U_out)


















