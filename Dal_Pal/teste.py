import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x, y = np.loadtxt("Precos.txt", delimiter=",", unpack=True)
f = interpolate.interp1d(x, y)

xnew = np.arange(1, 10, 0.1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`

plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()
