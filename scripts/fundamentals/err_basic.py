# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:53:10 2020
Error Handling
@author: Ashish
"""
try:
    number = float(input("Enter a number: "))
    print("The number is: ", number)
except:
    print("Invalid number")
