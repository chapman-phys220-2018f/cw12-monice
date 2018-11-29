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

import numpy as np
import numba as nb
import matplotlib.pyplot as plt
import sombrero as smb

def test_sombrero1():
    assert smb.sombrero(-.9,0,np.arange(0, 2*np.pi*50, 0.001), .18)[-1] < -0.8162394463974044
    assert smb.sombrero(-.9,0,np.arange(0, 2*np.pi*50, 0.001), .18)[-1] > -0.8162594463974044