#!/usr/bin/python2

import math
import numpy as np
import matplotlib.pyplot as plt

## Use a maximal value of f to avoid overflows
maxvalue = 10

f = lambda p: 1
g = lambda p: (1 - p)/p if p > 0 else float("inf")
fgmin = lambda p: min(f(p), g(p))

xmax = 20
ymax = 6
cstep = 0.2
cs = np.arange(cstep, 4 + 2*cstep, cstep)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

delta = 0.01
domain  = np.arange(0, 1 + delta, delta)

fplot  = plt.plot(domain, map(f, domain),
                   linestyle = "--", color = "g",
                   label = "$1$")
gplot  = plt.plot(domain, map(g, domain),
                   linestyle = "--", color = "r",
                   label = "$q/p$")
fgplot = plt.plot(domain, map(fgmin, domain),
                   linestyle = "-", color = "b",
                   label = "$P_1 = \\min\\{ 1, q/p \\}$")

plt.legend()

plt.xlim(0, 1)
plt.ylim(0, 2)
plt.savefig("P1.png", bbox_inches = "tight")
