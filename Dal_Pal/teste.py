import os
os.system('clear')

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


x, y = np.loadtxt("Precos.txt", delimiter=",", unpack=True)
f = interpolate.interp1d(x, y)

ynew = f(xnew)

plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()