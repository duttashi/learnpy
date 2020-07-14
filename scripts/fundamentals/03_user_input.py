# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:22:31 2020
Getting user input
@author: Ashish
"""
name = input("Enter your name: ")
print(name)
# -- Mathematics on user input --

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8  # Make sure this is correct
print(f"{square_feet} square feet is {square_metres} square metres.")
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")

