# Scipy examples

This directory contains several script that show how scipy can be used for particular scientific applications.
Also, you can look at an [extended list of Scipy Tutorials](https://docs.scipy.org/doc/scipy/reference/tutorial/) to go further ...

## [dataRegressionLSOptim.py](dataRegressionLSOptim.py)

This script performs a regression using non-linear least-square optimization extract a behavior law from noisy data.
In particular, it uses the [minimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) function of the scipy package.

## [jacobMultiDim.py](jacobMultiDim.py)

This script focus on the Jacobi matrix of the advection operator:

```math
f(u) = c_x \frac{\partial u}{\partial x}
```

It compute it in 1D, 2D, 3D, and extract the eigenvalues for each cases.
in particular, it uses the [eigvals](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvals.html) of the scipy package.