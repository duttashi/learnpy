# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 08:26:00 2020

Objective: Create a program that asks the user for 8 names of people
and stores them in a list. When all the names have been given,
pick a random name and print it.

@author: Ashish
"""
print("People names program ")
print("Enter name of 8 people")
# declare empty list
ppl_names = []
count = 0
resp = True
while resp:
    ppl_name = input()
    ppl_names.append(ppl_name)
    count+=1
    if (count<8):
        continue
    else:
        resp= False

# for name in ppl_names:
#     print(name)

# Now, pick a random name from the list and print it
import random
print("A random name from the list of people name is: ", 
      random.choice(ppl_names))
        
    

