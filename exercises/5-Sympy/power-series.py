#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Exercise 5.1: Sympy power series
#
# Complete the function powerSeries to compute, given a natural number a,
# the value of the following series:
#
#   oo      1
#  Sum  --------
# k = 1  k^(2*a)
#
# Use the functions Sum and limit of the sympy package:
#    Sum:   [http://docs.sympy.org/latest/_modules/sympy/concrete/summations.html#Sum]
#    limit: [http://docs.sympy.org/latest/modules/series/series.html#sympy.series.limits.limit]


import sympy as sy


def powerSeries(a):
    k = sy.symbols('k')
    n = sy.symbols('n')
    
    pass # Your code here


print(powerSeries(1))
print(powerSeries(2))
print(powerSeries(3))
