#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Compute the eigenvalues of the 1D, 2D and 3D advection operator when a finite
difference scheme is used to compute the space derivative
"""
import numpy as np
import scipy.linalg as spl
import matplotlib.pyplot as plt

# Matplotlib : do not fill marker in plot
plt.rcParams['markers.fillstyle'] = 'none'

# Number of point in each direction
nX = 12
nY = 12
nZ = 12

# Velocity in each direction
cX = 1.0
cY = 1.0
cZ = 1.0

# Discretization scheme in each direction
schemeX = 'U1'
schemeY = 'U1'
schemeZ = 'U1'

# Script actions
plotMatrix = True
saveFig = False

# Initial velocity fields
u01D = np.ones(nX)
u02D = np.ones((nX, nY)).ravel()
u03D = np.ones((nX, nY, nZ)).ravel()

# Stencils form definition
stencilU1 = [-1, 1, 0]
stencilC2 = [-0.5, 0, 0.5]
stencilU3 = [1./6, -6./6, 3./6, 2./6, 0]

dicoStencil = {'U1': ['$1^{st}$ order Upwind', stencilU1],
               'C2': ['$2^{nd}$ order Centered', stencilC2],
               'U3': ['$3^{rd}$ order Upwind', stencilU3]}

# Set stencils
stencilXName = dicoStencil[schemeX][0]
stencilYName = dicoStencil[schemeY][0]
stencilZName = dicoStencil[schemeZ][0]

stencilX = dicoStencil[schemeX][1]
stencilY = dicoStencil[schemeY][1]
stencilZ = dicoStencil[schemeZ][1]

iSX = (len(stencilX)-1)//2
iSY = (len(stencilY)-1)//2
iSZ = (len(stencilZ)-1)//2


def rhs1D(u):
    """
    Define a 1D Right Hand Side (RHS) for the advection operator

    .. math::
        f(u) = c_x \\frac{\\partial u}{\\partial x}

    The space derivative is approximated by a finite difference scheme,
    set depending on the value for the variable **schemeX** above in the
    script :

        - schemeX='U1': :math:`1^{st}` order upwind,

          .. math::
              \\frac{\\partial u_i}{\\partial x} \\simeq
              \\frac{u_{i}-u_{i-1}}{\\Delta_x}

        - schemeX='C2': :math:`2^{nd}` order centered,

          .. math::
              \\frac{\\partial u_i}{\\partial x} \\simeq
              \\frac{u_{i+1}-u_{i-1}}{2\\Delta_x}

        - schemeX='U3': :math:`3^{rd}` order upwind,

          .. math::
              \\frac{\\partial u_i}{\\partial x} \\simeq
              \\frac{2u_{i+1}+3u_{i}-6u_{i-1}+u_{i-2}}{6\\Delta_x}

    Parameter
    ---------
    u : numpy.ndarray
        The 1D vector, to evaluate the space derivative from,
        of size :math:`n_x`

    Returns
    -------
    uEval : numpy.ndarray
        The 1D derivative of u
    """
    u1D = u.reshape((nX))
    uEval = np.zeros_like(u1D)
    for i in range(len(stencilX)):
        uEval -= stencilX[i]*np.roll(u1D, iSX-i, axis=0)*cX

    return uEval.ravel()


def rhs2D(u):
    """
    Define a 2D Right Hand Side (RHS) for the advection operator

    .. math::
        f(u) = c_x \\frac{\\partial u}{\\partial x} +
        c_y \\frac{\\partial u}{\\partial y}

    See rhs1D for description of the space discretization

    Parameter
    ---------
    u : numpy.ndarray
        The 2D vector, to evaluate the space derivative from,
        of size :math:`n_x.n_y`

    Returns
    -------
    uEval : numpy.ndarray
        The 2D derivative of u
    """
    u2D = u.reshape((nX, nY))
    uEval = np.zeros_like(u2D)

    for i in range(len(stencilX)):
        uEval -= stencilX[i]*np.roll(u2D, iSX-i, axis=0)*cX
    for i in range(len(stencilY)):
        uEval -= stencilY[i]*np.roll(u2D, iSY-i, axis=1)*cY

    return uEval.ravel()


def rhs3D(u):
    """
    Define a 3D Right Hand Side (RHS) for the advection operator

    .. math::
        f(u) = c_x \\frac{\\partial u}{\\partial x} +
        c_y \\frac{\\partial u}{\\partial y} +
        c_z \\frac{\\partial u}{\\partial z}

    See rhs1D for description of the space discretization

    Parameter
    ---------
    u : numpy.ndarray
        The 3D vector, to evaluate the space derivative from,
        of size :math:`n_x.n_y.n_z`

    Returns
    -------
    uEval : numpy.ndarray
        The 3D derivative of u
    """
    u3D = u.reshape((nX, nY, nZ))
    uEval = np.zeros_like(u3D)

    for i in range(len(stencilX)):
        uEval -= stencilX[i]*np.roll(u3D, iSX-i, axis=0)*cX
    for i in range(len(stencilY)):
        uEval -= stencilY[i]*np.roll(u3D, iSY-i, axis=1)*cY
    for i in range(len(stencilZ)):
        uEval -= stencilZ[i]*np.roll(u3D, iSZ-i, axis=2)*cZ

    return uEval.ravel()


def computeJacobian(u, rhs):
    """
    Compute the Jacobi matrix of a given RHS function, by computing the
    partial derivative with finite difference for every element of the
    vectorial basis.

    Parameter
    ---------
    u : numpy.ndarray
        The initial vector, where to evaluate
    """
    n = u.size
    uPerturb = u.copy()
    jacobian = np.empty((n, n))
    uEval0 = rhs(u)
    eps = 1e-8
    for i in range(n):
        uPerturb[i] += eps
        jacobian[:, i] = rhs(uPerturb)
        jacobian[:, i] -= uEval0
        jacobian[:, i] /= eps
        uPerturb[i] = u[i]
    return jacobian


# Compute the Jacobie matrix of each RHS function
print('Compute 1D Jacobi matrix')
A1D = computeJacobian(u01D, rhs1D)
print('Compute 2D Jacobi matrix')
A2D = computeJacobian(u02D, rhs2D)
print('Compute 3D Jacobi matrix')
A3D = computeJacobian(u03D, rhs3D)

# Eventually plot the Jacobi matrices
if plotMatrix:
    plt.figure('1D')
    plt.imshow(A1D)
    plt.colorbar()

    plt.figure('2D')
    plt.imshow(A2D)
    plt.colorbar()

    plt.figure('3D')
    plt.imshow(A3D)
    plt.colorbar()

# Compute the eigenvalues of each Jacobi matrix
print('Compute eigenvalues of 1D Jacobi matrix')
lam1D = spl.eigvals(A1D)
print('Compute eigenvalues of 2D Jacobi matrix')
lam2D = spl.eigvals(A2D)
print('Compute eigenvalues of 3D Jacobi matrix')
lam3D = spl.eigvals(A3D)
print('Done, ploting ...')

# Plot the eigenvalues
plt.figure('Eigenvalues')
plt.axvline(0, c='gray', ls='--', lw=1.0)
plt.axhline(0, c='gray', ls='--', lw=1.0)
plt.plot(lam1D.real, lam1D.imag, 's', label='1D', ms=12.0, mfc=None)
plt.plot(lam2D.real, lam2D.imag, 'o', label='2D', ms=8.0, mfc=None)
plt.plot(lam3D.real, lam3D.imag, '*', label='3D', ms=6.0, mfc=None)
plt.axis('equal')
plt.legend()
plt.xlabel('$\\mathcal{R}(\\lambda)$')  # Use $...$ for latex output
plt.ylabel('$\\mathcal{I}(\\lambda)$')

# Define figure title
if stencilXName == stencilYName and stencilYName == stencilZName:
    stencilName = stencilXName
else:
    stencilName = '{}(x), {}(y), {}(z)'.format(
        stencilXName, stencilYName, stencilXName)

plt.title('Eigenvalues of '+stencilName+' operator (Advection)\n' +
          'cX={}, cY={}, cZ={}'.format(cX, cY, cZ))

# Eventually save figure
if saveFig:
    if schemeX == schemeY and schemeY == schemeZ:
        scheme = schemeX
    else:
        scheme = schemeX+schemeY+schemeZ
    plt.savefig('eigenvalues{}.pdf'.format(scheme), bbox_inches='tight')

# Show plot
plt.show()
