import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy import constants
import random

# https://stackoverflow.com/questions/31303601/animate-a-python-pyplot-by-moving-a-point-plotted-via-scatter/38126963



class chargePoint:
    q = None
    m = None
    f = None
    p = None
    def __init__(self):
        self.q = constants.e
        self.m = constants.m_e
        self.f = np.zeros((1,3))
        self.p = np.zeros((1,3))

    def getCharge(self):
        return self.q

    def getMass(self):
        return self.m

    def applyForce(F):
        self.f = F

    def getForce(self):
        return self.f

    def setPosition(pos):
        self.p = pos

    def getPosition(self):
        return self.p

    def calcNewPosition(self):
        return 0


def getCoulombForce(pos_m,
                    pos_n,
                    q_m,
                    q_n):
    k_e = 1 / (4*np.pi*constants.epsilon_0)
    # calculate distance vector between the two charges
    r_mn = pos_m - pos_n
    r_mn_norm = np.linalg.norm(r_mn)
    r_mnh = r_mn / r_mn_norm
    return k_e * q_m * q_n / r_mn_norm**2 * r_mnh


charge_0_pos = np.array([[1],[1]])
charge_1_pos = np.array([[0.5],[0.5]])


print(getCoulombForce(charge_0_pos,
                      charge_1_pos,
                      constants.e,
                      constants.e))


# boundaries 
x_min = -1
y_min = -1
z_min = -1
x_max = 1
y_max = 1
z_max = 1


print(random.uniform(x_min,x_max))

charges = []

for i in range(5):
    qt = chargePoint()
    p_rand = [[random.uniform(x_min,x_max)],
              [random.uniform(y_min,y_max)],
              [random.uniform(z_min,z_max)]]
    
    print(p_rand)
    
    # TODO: initialize charge with random position within a given boundary
    #qt.setPosition(p_rand)
    
    charges.append(qt)
    print(charges[i].getMass())
