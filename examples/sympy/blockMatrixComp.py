# -*- coding: utf-8 -*-
"""
Performs block matrix computations, and print latex formula
"""
import sympy as sy
sy.init_printing()

# Define symbolds
A, B, C = sy.symbols('A, B, C', commutative=False)
D = sy.symbols('D', commutative=True)

M = sy.Matrix([[D, B, 0],
               [C, D, 0],
               [0, 0, A]])

# Compute symbolic operations
M1 = M**2
M1.simplify()

M2 = (M-sy.eye(3))*M
M2.simplify()

# Print latex formula
print('M1 = ')
print(sy.latex(M1))
print('M2 = ')
print(sy.latex(M2))
