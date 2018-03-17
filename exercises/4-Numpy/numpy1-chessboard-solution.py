#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercise 4.1: Numpy chessboard - Solution
#
# Create a 8x8 matrix with a chessboard pattern with numbers 1 and 0.

import numpy as np

def chessboard():
    M = np.zeros((8,8))
    
    for i in np.arange(0,8):
        for j in np.arange(0,8):
            M[i, j] = (i + j) % 2
    
    return M


print(chessboard())
