# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:58:11 2020

@author: Ashish
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20,1000)
y = np.sin(x)+.2*x

plt.plot(x,y)
plt.xlabel("input")
plt.ylabel("output")
plt.title("my plot")
plt.show()

# Scatterplt
X = np.random.randn(100,2)
plt.scatter(X[:,0],X[:,1])
plt.show()

X = np.random.randn(200,2)
X[:50]+=3
Y = np.zeros(200)
Y[:50]=1
plt.scatter(X[:,0],X[:,1], c=Y)
plt.show()

# Histogram
# used for plotting distribution of data
X = np.random.randn(10000)
plt.hist(X, bins=50);
plt.show()

X = np.random.random(10000)
plt.hist(X, bins=50);
plt.show()

# plotting images



