#/usr/bin/env python
#coding: utf-8
import os
os.system('clear')

import scipy

x = 1
y = 2

a = scipy.stat.kendall stats.kendalltau(x, y, initial_lexsort=True)

print (a)
