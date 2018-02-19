# Simple tool for solving limiting distributions of markov chains
# by Matthew Lynn, github hyper-mage

import numpy as np
from fractions import Fraction

# Use these 'M' variables as example when making your own if needed.
# Simply comment out the other 'M' lines with ctrl+/
# M = np.array([[1/10, 9/10, 0, 0], [2/9, 0, 7/9, 0], [3/7, 0, 0, 4/7], [1, 0, 0, 0]])
# M = np.array([[.5, .4, .1], [.9, .1, 0], [.2, 0, .8]])
# M = np.array([[.5, .3, .2], [.1, .7, .2], [.1, .8, .1]])
# M = np.array([[.9, .1, 0], [0, .8, .2], [1, 0, 0]])
# M = np.array([[.7, .2, .1], [.2, .6, .2], [.1, .4, .5]])
M = np.array([[.9, .1, 0, 0], [.6, 0, .4, 0], [.3, 0, 0, .7], [.2, 0, 0, .8]])
print(M)
# 128 should be plenty, but if not just bump it up to 256
# note: this can also be used to solve time step probabilities
L = np.linalg.matrix_power(M, 128)
print(L)
# Bump the range (0,n+1) up to n+1 where n is the size of your nxn square matrix
# Don't ask me why it's n+1 because idk
for x in range(0, 4):
    print(Fraction(L[0][x]).limit_denominator(10000))