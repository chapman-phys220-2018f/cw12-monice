#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import numba as nb

###
# Name: Abby Wheaton, Monica Hiemer, and Royal Cuevas
# Student ID: 2299246
# Email: wheaton@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW11
###


@nb.jit
def dxdt(x, y, t):
    return y

@nb.jit
def dydt(x, y, t, F):
    return x-x**3-0.25*y + F*np.cos(t)

@nb.jit
def sombrero(x0, y0, t, F):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    dt = t[1]-t[0]
    x[0] = x0
    y[0] = y0    
    for i in range(1, len(t)): 
        x1 = dt*dxdt(x[i-1], y[i-1], t[i-1])
        x2 = dt*(dxdt(x[i-1], y[i-1], t[i-1])+x1/2)
        x3 = dt*(dxdt(x[i-1], y[i-1], t[i-1])+x2/2)
        x4 = dt*(dxdt(x[i-1], y[i-1], t[i-1])+x3)
        x[i] = x[i-1]+(x1+2*x2+2*x3+x4)/6
        y1 = dt*dydt(x[i-1], y[i-1], t[i-1], F)
        y2 = dt*(dydt(x[i-1], y[i-1], t[i-1], F)+y1/2)
        y3 = dt*(dydt(x[i-1], y[i-1], t[i-1], F)+y2/2)
        y4 = dt*(dydt(x[i-1], y[i-1], t[i-1], F)+y3/3)
        y[i] = y[i-1]+(y1+2*y2+2*y3+y4)/6
        
    plt.plot(t,x)
    plt.plot(t,y)
        
    return x
        
        