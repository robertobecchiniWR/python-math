#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 4.2: Numpy matrix order
#
# Complete the function order to find the order of a 2x2 matrix modulo n.
# Assume that the matrix has nonzero determinant.
# Use the function np.array_equal(M1, M2) for matrix comparison.

import numpy as np

def order(M, n):
    pass # Your code here


A = 3 * np.eye(2)
B = np.array([[0, 1], [1, 0]])
C = np.array([[1, 2], [3, 4]])

print(order(A, 2))
print(order(B, 3))
print(order(C, 7))
