# Sympy examples

This directory contains several script that show how sympy can be used for particular scientific applications.
Also, you can look at an [extended list of Sympy Tutorials](http://docs.sympy.org/latest/tutorial/index.html) to go further ...

## [solve-diff-eqns.py](solve-diff-eqns.py)

This script is a basic example of how to solve a differential equation using sympy.

In particular, the equation u''(t) - u(t) = exp(t) is solved, using the sympy function [dsolve](http://docs.sympy.org/latest/modules/solvers/ode.html).

## [blockMatrixComputation.py](blockMatrixComputation.py)

Performs block matrix computation with non-comuutative blocks, and print latex output for the results

## [generalMidPointInterpolation.py](generalMidPointInterpolation.py)

This script compute the general formula of mid-point interpolation on one-dimensionnal uniform grids.
The interpolation can be computed for any order (1, 3, 5, ... always an odd number) 
