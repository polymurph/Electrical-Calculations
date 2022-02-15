import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy import constants
import random

# https://stackoverflow.com/questions/31303601/animate-a-python-pyplot-by-moving-a-point-plotted-via-scatter/38126963

# https://likegeeks.com/3d-plotting-in-python/

class chargePoint:
    q = None
    m = None
    f = None
    p = None
    def __init__(self):
        self.q = constants.e
        self.m = constants.m_e
        self.f = np.zeros((1,3))
        self.p = np.array(np.zeros((1,3)))

    def getCharge(self):
        return self.q

    def getMass(self):
        return self.m

    def applyForce(self,F):
        self.f = F

    def getForce(self):
        return self.f

    def setPosition(self,pos):
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


charge_0_pos = np.array([[1],[1],[1]])
charge_1_pos = np.array([[0.5],[0.5],[0.5]])


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

charges = []

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

def showPositions(charge_list):
    for i in range(len(charge_list)):
        point = charges[i].getPosition()
        ax.scatter(point[0],point[1],point[2])
    plt.show()

for i in range(5):
    qt = chargePoint()
    p_rand = [[random.uniform(x_min,x_max)],
              [random.uniform(y_min,y_max)],
              [random.uniform(z_min,z_max)]]
    
    # TODO: initialize charge with random position within a given boundary
    qt.setPosition(np.array(p_rand))
    # append new charge to array
    charges.append(qt)
    #point = charges[i].getPosition()
    #ax.scatter(point[0],point[1],point[2])

#plt.show()

showPositions(charges)

