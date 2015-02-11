#!/usr/bin/python2

import math
import numpy
import matplotlib.pyplot as plt

## Use a maximal value of f to avoid overflows
maxvalue = 10

f = lambda u: min(math.pow(math.sqrt(2), u), maxvalue)

def sequence_b(c, n):
    result = []
    while len(result) < n:
        result.append(c)
        c = f(c)
    return(result)

xmax = 20
ymax = 6
cstep = 0.2
cs = numpy.arange(cstep, 4 + 2*cstep, cstep)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for c in cs:
    plt.plot(range(1, xmax+1),
             sequence_b(c, xmax))

plt.xlim(1,xmax)
plt.ylim(0,ymax)
plt.savefig("infinite_exponentiation.png", bbox_inches = "tight")
