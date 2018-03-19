#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:54:50 2016

@author: t.lunet
"""
import sympy as sy
from time import time
sy.init_printing()

# Interpolation order : 1, 3, 5, ... always odd number
nP = 1

# Setup computations
i0 = (nP-1)//2
A = sy.zeros(nP+1)
e = sy.ones(1, nP+1)

# Construction of dX symbols
lDx = []
for i in range(nP):
    lDx.append(sy.Symbol('\\Delta x_{'+str(i-i0)+'}'))
lPos = [0]*(nP+1)
lPos[i0] = 0
for i in range((nP-1)//2):
    lPos[i0-i-1] = lPos[i0-i]-lDx[i0-i-1]
for i in range((nP+1)//2):
    lPos[i0+i+1] = lPos[i0+i]+lDx[i0+i]

# Contruct vandermonde matrix
for i in range(nP+1):
    c = i-i0
    for j in range(nP+1):
        A[i, j] = c**j

# Coordinate for middle point
for i in range(nP+1):
    e[0, i] /= 2**i


print('Inverting A')
t0 = time()
coeff = e * A.inv()
print(' -- computation time = {:.2f}'.format(time()-t0))

print('Simplifying coeff')
t0 = time()
coeff.simplify()
print(' -- computation time = {:.2f}'.format(time()-t0))
