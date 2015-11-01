#!/usr/bin/python2

import math
import numpy as np
import matplotlib.pyplot as plt

f = lambda n: (1 - 1.0/n)**n
g = lambda n: math.exp(-1)
h = lambda n: math.exp(-1) * 0.99

xmax = 100
ymax = 0.41

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

domain  = np.arange(1, xmax + 1)

fplot  = plt.plot(domain, map(f, domain),
                   linestyle = "-", color = "b",
                   label = "$\\left( 1 - \\frac{1}{n} \\right)^{n}$")
gplot  = plt.plot(domain, map(g, domain),
                   linestyle = "--", color = "r",
                   label = "$e^{-1}$")
hplot  = plt.plot(domain, map(h, domain),
                   linestyle = ":", color = "r",
                   label = "$0.99 \cdot e^{-1}$")

plt.legend()

plt.xlim(1, xmax)
plt.ylim(0.25, ymax)
plt.savefig("counterfeit.png", bbox_inches = "tight")

# for i in domain:
#     if f(i) > h(i):
#         print(i)
