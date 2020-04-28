# Objective: Introduction to Numpy. Understanding it for data analysis
# Reference: https://www.machinelearningplus.com/python/numpy-tutorial-part1-array-python-examples/

import numpy as np

# There are many ways to create a numpy array. The most common one is to create a list and then pass it into `np.array()` function
list1=[1,2,3,4]
print("list and its type", type(list1))
arr1= np.array(list1)
print(type(arr1))

# A list cannot handle math operations while a numpy array can
#list1+2 will give error
print(arr1+2)

# create a 2d array
list2 = [[0,1,22],[3,4,5]]
print(list2)
print(np.array(list2))
# specify the datatype by setting the dtype argument
list2 = [[0,1,22],[3,4,5]]
print(np.array(list2, dtype=float)) # The decimal point after each number is indicative of the float datatype.

# You can also convert it to a different datatype using the astype method.
arr2d = np.array(list2)
print(arr2d.astype(str))

# if you are uncertain about what datatype your array will hold or if you want to hold characters and numbers in the same array, you can set the dtype as 'object'.
# create an array to hold numbers and strings
arr2d_obj = np.array([1,2.3,4.4,100,'cat','bat'], dtype=object)
print(arr2d_obj)

# Finally, you can always convert an array back to a python list using tolist().
print(arr2d_obj.tolist())

# How to check the array shape and size?
# In R, use dim() for dimesnions and shape()
# In Python use, ndim(), to check if its 1D or 2D array;
# In python use, shape(), to check how many items are present in each dimension.
# In python use, dtype(), to check the data type
# In python use, size(), to check the size of array
# In python use, shape(), to sample a first few items through indexing
print(arr2d.ndim)
print(arr2d_obj.shape)
print(arr2d_obj.dtype)
print(arr2d_obj.size)
#print(arr2d_obj.sample)

# How to extract specific elements from a numpy array. Use the : notation
list3 = [10,20,30,40]
arr2 = np.array(list3)
x = arr2[:4]
print(x)

# reverse the rows and the whole array. Use :: notation
print(arr2[::-1]) # reverse only the rows
list4 = [[1,2,3,4],[5,6,7,8]]
arr3 = np.array(list4, dtype=float)
print(arr3[::-1,::-1])

# Missing values can be represented using np.nan object, while np.inf represents infinite.
# Insert a nan and an inf
arr3[1,1] = np.nan  # not a number
arr3[1,2] = np.inf  # infinite
print(arr3)

# How to compute mean, min, max on the ndarray?
list5 = [[1,2,3,4],[5,6,7,8]]
arr4 = np.array(list5)
print("Mean value is ", arr4.mean())
print("Min value is ", arr4.min())
print("Max value is ", arr4.max())

# How to compute row-wise and col-wise mean? Use np.amin()
print("Row wise min is ", np.amin(arr4, axis=0))
print("Col wise min is ", np.amin(arr4, axis=1))

