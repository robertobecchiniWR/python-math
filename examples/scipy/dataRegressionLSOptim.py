#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Perform a non-linear regression for noisy data, using the optimize function
of scipy
"""
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

# Matplotlib : do not fill marker in plot
plt.rcParams['markers.fillstyle'] = 'none'

# Define an exponential law for x data
alphaTh = 0.6
betaTh = 0.9


def expoLaw(x, alpha=alphaTh, beta=betaTh):
    """
    Define an exponential law of the form

    .. math::
        f(x) = \\alpha e^{\\beta x}

    Parameters
    ----------
    x : numpy.ndarray, or float, or int
        The x to evaluate, eventualy in vectorial form
    alpha : float
        The :math:`\\alpha` coefficient, default value is defined
        above in the script
    beta : float
        The :math:`\\beta` coefficient, default value is defined
        above in the script
    """
    return alpha*np.exp(beta*x)


# Build noisy data
nMeasure = 50
noiseAmplitude = 0.09
xMeasure = np.linspace(0, 1, num=nMeasure)
yMeasure = expoLaw(xMeasure) + np.random.randn(nMeasure)*noiseAmplitude


def functionToMinimize(x):
    """
    Define a function to minimize in order to determine
    alpha, beta coefficients for the exponential law, given the
    vector of noisy data **yMeasure** (:math:`y_m`) and the x data coordinates
    **xMeasure** (:math:`x_m`):

    .. math::
        f(\\alpha, \\beta) = || \\alpha e^{\\beta x_m} - y_m||_2
    """
    alpha = x[0]
    beta = x[1]
    return np.linalg.norm(expoLaw(xMeasure, alpha, beta) - yMeasure)


res = sco.minimize(functionToMinimize, [1.0, 1.0])

# The minimize function returns a dictionnary:
print(res)

# Get alpha and beta obtained from the minimization
alphaExp = res['x'][0]
betaExp = res['x'][1]

# Plot data
plt.figure('Data regerssion')
x = np.linspace(0, 1, num=200)
plt.plot(x, expoLaw(x), '-', label='Exact data')
plt.plot(xMeasure, yMeasure, 'o', label='Noisy data')
plt.plot(x, expoLaw(x, alphaExp, betaExp), 's--',
         label='Regression data', markevery=0.1)
plt.legend()
plt.show()
