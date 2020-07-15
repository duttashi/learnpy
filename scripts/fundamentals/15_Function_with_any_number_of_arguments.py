# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:45:59 2020
@author: Ashish

Objective: Unpacking Arguments

"""
# define a function
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total*arg
    return total
    #print(total)
    
# Call the function
print(multiply(1,2,3,4,5))
print(multiply(1,2))


