# -*- coding: utf-8 -*-
"""
Perform the Rutishauser-Kahan-Pal-Walker algorithm, using pure python
and pure fortran.

This algorithm allows to transform a matrix of the form

[    1    sqrt(w1) sqrt(w2) ... sqrt(wn)]
[sqrt(w1)   tau1                        ]
[sqrt(w2)            tau2               ]
[  :                        ...         ]
[sqrt(wn)                         taun  ]

into the tridiagonal matrix

[    1    sqrt(b0)                                 ]
[sqrt(b0)    a0    sqrt(b1)                        ]
[         sqrt(b1)    a1     sqrt(b2)              ]
[                    ...        ...        ...     ]
[                            sqrt(b{n-1})   a{n-1} ]

using givens rotations.


NOTE: This example assumes that your OS has some Fortran compiler installed.
      You can download one at [https://gcc.gnu.org/wiki/GFortranBinaries].
"""
import os
import subprocess
import numpy as np
from time import time


# Define Python function
def tridiag_rpkw_python(nodes, weights):

    n = nodes.size

    alpha = np.array(nodes)
    beta = np.zeros(n)
    beta[0] = weights[0]

    for i in range(n-1):

        pi2 = weights[i+1]
        lam = nodes[i+1]

        gamma2 = 1.
        sigma2 = 0.
        tau = 0.

        for k in range(i+2):

            oldBeta = beta[k]
            rho2 = oldBeta + pi2
            beta[k] = gamma2*rho2
            oldSigma2 = sigma2

            if rho2 == 0:
                gamma2 = 1.
                sigma2 = 0.
            else:
                gamma2 = oldBeta/rho2
                sigma2 = pi2/rho2

            newTau = sigma2*(alpha[k]-lam) - gamma2*tau
            alpha[k] = alpha[k] - (newTau-tau)
            tau = newTau

            if sigma2 == 0:
                pi2 = oldSigma2*beta[k]
            else:
                pi2 = tau**2/sigma2

    return alpha, beta


# Compile fortran function
print('Compiling fortran library')
cmd = 'f2py -c -m libfor libfor.f95'
with open(os.devnull, 'wb') as devnull:
    subprocess.check_call(
        cmd.split(), stdout=devnull, stderr=subprocess.STDOUT,
        env=os.environ.copy())
print(' -- done')


# Define fortran function
def tridiag_rpkw_fortran(nodes, weights):

    # Import fortran library
    import libfor

    # Prepare input and output arrays
    nodes = np.asarray(nodes)
    weights = np.asarray(weights)
    n = nodes.size
    alpha = np.empty(n)
    beta = np.empty(n)

    # Call fortran library
    libfor.tridiag_rpkw(nodes, weights, alpha, beta, n)

    return alpha, beta


# Performance test
def runPerfo(nPoints):
    print('Running performance test with a {0}x{0} matrix'.format(nPoints+1))

    # Create nodes and weights
    weights = np.full(nPoints, 1./nPoints)
    nodes = np.linspace(-1, 1, num=nPoints, endpoint=False) + 1./nPoints/2.

    # Python run
    tBeg = time()
    alpha, beta = tridiag_rpkw_python(nodes, weights)
    tEnd = time()
    tPython = tEnd - tBeg
    print(' -- python routine: {:f}s'.format(tPython))

    # Fortran run
    tBeg = time()
    alpha, beta = tridiag_rpkw_fortran(nodes, weights)
    tEnd = time()
    tFortran = tEnd - tBeg
    print(' -- fortran function: {:f}s'.format(tFortran))
    print(' -- speedUp factor: {:f}'.format(tPython/tFortran))


runPerfo(100)
runPerfo(500)
runPerfo(1000)
