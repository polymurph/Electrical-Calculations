#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:37:11 2021

@author: ed
"""

import numpy as np
import scipy as sp


class ChargedPoint:
    def __init__(charge, x, y):
        self.charge = charge
        self.x = x
        self.y = y
    
        