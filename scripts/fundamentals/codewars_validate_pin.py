# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:39:53 2020
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
@author: Ashish
"""

def validate_pin(pin):
    if( len(pin)==4 ):
        return True
    elif( len(pin)==6):
        return True
    else:
        return False
    
num = input("Enter your 4 digit pin: ")
resp = validate_pin(num)
print(resp)