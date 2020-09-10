# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:13:31 2020
reverse a string.
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
@author: Ashish
"""

# method 1
def approach_1(str):
    return(str[::-1])

# method 2
def approach_2(string):
    newstring = ""
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter -1 
    return newstring

# method 3
def approach_3(string):
    y = ""
    for i in string:
        y = i+y
    return y

# Test the approaches
print(approach_1('hello'))
print(approach_2("Good Bye"))
print(approach_3("Mission Impossible"))
