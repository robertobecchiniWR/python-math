#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 09:49:39 2018

@author: lunet
"""
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

x = np.linspace(0, 1, num=200)

alphaTh = 0.6
betaTh = 0.9


def law(x, alpha=alphaTh, beta=betaTh):
    return alpha*np.exp(beta*x)


nMeasure = 50
noiseAmplitude = 0.08
xMeasure = np.linspace(0, 1, num=nMeasure)
yMeasure = law(xMeasure) + np.random.randn(nMeasure)*noiseAmplitude


def minFunc(alpha, beta):
    return np.linalg.norm(law(xMeasure, alpha, beta))

sco.minimize


plt.figure('Data regerssion')
plt.plot(x, law(x), '-', label='Exact data')
plt.plot(xMeasure, yMeasure, 'o', label='Noisy data')
plt.legend()
plt.show()