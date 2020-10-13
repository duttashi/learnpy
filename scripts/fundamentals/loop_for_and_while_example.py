# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:06:20 2020

@author: Ashish
For and while loops
"""

# declare a list of items
subjects = ['math','science','arts','social-science']

for i in range(len(subjects)):
    # prints the length of each string in the list
    print(len(subjects[i]))
print("##########################")    
for n, alpha in enumerate(subjects):
    print(alpha, n)
print("##########################")
for i in range(len(subjects)):
    for n, alpha in enumerate(subjects[i]):
        print(alpha, n)

