# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:31:07 2020

@author: Ashish
"""

def get_sum(a,b):
    numsum=0
            
    for i in range(a,b+1):
        numsum+=i
        
    return numsum

print(get_sum(0,1))


    
