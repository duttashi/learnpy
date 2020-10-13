# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:34:24 2020

@author: Ashish

Objective: Lambda basics
Aim: Use map() in lambda to make the code readable
"""
sequence = [1,2,3,4,5]
#doubled = [(lambda x: x*2)(x) for x in sequence]
doubled = map(lambda x: x*2, sequence)
print(doubled)


