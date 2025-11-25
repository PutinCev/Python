# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:06:25 2025

@author: TBG
"""
import math
import dilog

def calc():
    d1, d2, h, VSand, n, theta1 = dilog.ask()
    d1 = d1 * 3
    x = d1 * math.tan(theta1 * 0.0174533)
    h = h * 3;
    VSand = VSand * 1.46667
    L1 = math.sqrt(pow(x, 2) + pow(d1, 2))
    L2 = math.sqrt(pow((h - x), 2) + pow(d2, 2))
    t = 1 / VSand * (L1 + n * L2)
    return t, theta1
    