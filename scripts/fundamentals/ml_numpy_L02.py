
# Objective: Read two csv files as separate numpy arrays and compute the average difference between the first table and the second table.

import numpy as np

tbl1 = np.genfromtxt('C:/Users/Ashoo/Documents/PythonPlayground/learnpy/data/data1.csv', delimiter=',', dtype=None, encoding=None)
tbl2 = np.genfromtxt('C:/Users/Ashoo/Documents/PythonPlayground/learnpy/data/data2.csv', delimiter=',', dtype=None, encoding= None)
print(tbl1)
print(tbl2)

# Objective: compute the average difference the above two numpy arrays
#np.mean(np.abs(tbl1[:, None]- tbl2))
print(np.isnan(tbl2).any())
chr
