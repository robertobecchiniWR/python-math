# -*- coding: utf-8 -*-
"""
Function that uses numpy to read and write file into text files
"""
import numpy as np

# Read data
data = np.loadtxt('data.txt', dtype=float)

# Extract specific data
x = data[:, 0]  # x is first column
f = data[:, 1]  # f is second column
g = data[:, 2]  # g is third column

# Print data
print('x = {}'.format(x))
print('f(x) = {}'.format(f))
print('g(x) = {}'.format(g))

# Multiply f and g by two
f2 = 2*f
g2 = 2*g

# Save modified data
dataOut = np.block([[x],
                    [f2],
                    [g2]]).T  # Concatenate data column wise
np.savetxt('data_double.txt', dataOut, fmt=('%.2f', '%2d', '%.2e'),
           header='X 2f(X) 2g(X)')
