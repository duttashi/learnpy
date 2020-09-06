# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:22:52 2020
create a factorial function
@author: Ashish
"""

def factorial(num):
    if (num>1):
        return num*factorial(num-1)
    else:
        return num
    
# call the function
print(factorial(999))

