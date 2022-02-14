import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy import constants

# https://stackoverflow.com/questions/31303601/animate-a-python-pyplot-by-moving-a-point-plotted-via-scatter/38126963



class chargePoint:
    q = None
    m = None
    f = None
    p = None
    def __init__(self):
        self.q = constants.e
        self.m = constants.m_e
        self.f = np.zeros((3,1))
        self.p = np.zeros((3,1))

    def getCharge(self):
        return self.q

    def getMass(self):
        return self.m

    def applyForce(F):
        self.f = F

    def getForce(self):
        return f

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


charges = []

for i in range(5):
    qt = chargePoint()
    charges.append(qt)
    print(charges[i].getMass())
