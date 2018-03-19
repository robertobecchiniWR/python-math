# Numpy examples

This directory contains several script that show how numpy can be used for particular scientific applications.

## [numpyIO.py](numpyIO.py)

Read and write data (matrix, vector, etc ...) with simple, efficient and beautiful one-line command.
In particular, this script uses the [loadtxt](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.loadtxt.html)
and [savetxt](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savetxt.html) numpy functions, to read the data stored
in the [data.txt](data.txt) file, modify those and write the modified data into [data_double.txt](data_double.txt).

## [callFortranRoutine.py](callFortranRoutine.py)

Perform the [Rutishauser-Kahan-Pal-Walker algorithm](https://link.springer.com/content/pdf/10.1007/BF01405565.pdf) to transform an arrow matrix (with non-zero elements
in the first row and column, and diagonal) into a symmetric trifdiagonal matrix.
It uses the [f2py](https://www.numfys.net/howto/F2PY/) sub-module of numpy to compile a fortran subroutine that can be called in python. 


## [csv-read-interpol-plot.py](csv-read-interpol-plot.py)

Read noisy data that are stored in a .csv file (comma separated values, like Excel files, ...), and build a polynomial that can fit the data.
In particular, it uses the [genfromtxt](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html) function to read
the .csv file, and the [polyfit](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.polyfit.html) to fit a polynomial to the noisy data.