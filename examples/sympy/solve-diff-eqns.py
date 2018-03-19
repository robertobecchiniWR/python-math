#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Sympy example: How to solve a differential equation using sympy 

@author: a.perez
"""

import sympy as sy

# Define a generic function u and its variable, t
u = sy.Function('u')
t = sy.symbols('t')

# We want to solve the differential equation u''(t) - u(t) = exp(t)

u_tt = sy.diff(u(t), t, t)  # Second derivative of u wrt t
                            # (symbolic, since u is a generic function)

lhs = u_tt - u(t)           # Left hand-side of the equation
rhs = sy.exp(t)             # Right hand-side of the equation

eq = sy.Eq(lhs, rhs)        # We create the equation


sol = sy.dsolve(eq, u(t))   # And we solve it using the function dsolve,
                            # wrt the function u(t)
                            
                            
# Now sol is the equation:
#   u(t) = C2*exp(-t) + (C1 + t/2)*exp(t)
