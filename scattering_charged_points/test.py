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
    
    def setCharge(self, q):
        self.q = q
        
    def getMass(self):
        return self.m

    def setMass(self,m):
        self.m = m

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


def calcChargeForce(q0,q1):
    k_e = 1 / (4*np.pi*constants.epsilon_0)
    # calculate distance vector between the two charges
    r_mn = q0.getPosition() - q1.getPosition()
    r_mn_norm = np.linalg.norm(r_mn)
    r_mnh = r_mn / r_mn_norm
    return k_e * q0.getCharge() * q1.getCharge() / r_mn_norm**2 * r_mnh

def showChargePositions(charge_list,index):
    fig = plt.figure(index)
    ax = fig.add_subplot(111, projection='3d')
    aa = 0.1
    ax.set_xlim([-aa,aa])
    ax.set_ylim([-aa,aa])
    ax.set_zlim([-aa,aa])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    for i in range(len(charge_list)):
        point = charges[i].getPosition()
        ax.scatter(point[0],point[1],point[2])
        p = charge_list[i].getPosition()
        ax.text3D(p[0][0],p[1][0],p[2][0],i)
    plt.title(index)
    plt.show()
    
def calcChargeForces(charge_list):
    rr = range(len(charge_list))
    for i in rr:
        f = np.zeros((3,1))
        for j in rr:
            if(i != j):
                f = f + calcChargeForce(charge_list[i],charge_list[j])
        charge_list[i].applyForce(f)

def updateChargepositions(charge_list, delta_t):
    rr = range(len(charge_list))
    for i in rr:
        f = charge_list[i].getForce()
        m = charge_list[i].getMass()
        pos_now = charge_list[i].getPosition()
        new_pos = pos_now + f / m * delta_t**2
        charge_list[i].setPosition(new_pos)


# boundaries 
x_min = -1
y_min = -1
z_min = -1
x_max = 1
y_max = 1
z_max = 1

charges = []

fig = plt.figure(figsize=(4,4))


"""
for i in range(10):
    qt = chargePoint()
    p_rand = [[random.uniform(x_min,x_max)],
              [random.uniform(y_min,y_max)],
              [random.uniform(z_min,z_max)]]
    
    # TODO: initialize charge with random position within a given boundary
    qt.setPosition(np.array(p_rand))
    qt.setMass(100)
    # append new charge to array
    charges.append(qt)
    #point = charges[i].getPosition()
    #ax.scatter(point[0],point[1],point[2])

"""

qt = chargePoint()
p_rand = np.array([[0.5],
          [1],
          [0.5]])
p_rand = p_rand * 0.02
# TODO: initialize charge with random position within a given boundary
qt.setPosition(np.array(p_rand))
qt.setMass(constants.m_e)
qt.setCharge(-constants.e)
# append new charge to array
charges.append(qt)

qt = chargePoint()
p_rand = np.array([[-0.5],
          [-1.5],
          [-0.5]])
p_rand = p_rand * 0.02
# TODO: initialize charge with random position within a given boundary
qt.setPosition(np.array(p_rand))
qt.setMass(constants.m_e)
qt.setCharge(-constants.e)
# append new charge to array
charges.append(qt)

qt = chargePoint()
p_rand = np.array([[0.8],
          [-1],
          [-1.5]])
p_rand = p_rand * 0.02
# TODO: initialize charge with random position within a given boundary
qt.setPosition(np.array(p_rand))
qt.setMass(constants.m_e)
qt.setCharge(-constants.e)
# append new charge to array
charges.append(qt)

delta_t = 0.0001


fig_index = 0

for i in range(100):
    showChargePositions(charges,fig_index)
    calcChargeForces(charges)
    updateChargepositions(charges, delta_t)
    fig_index = fig_index + 1


