# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 07:03:09 2020
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array 

Reference: https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
@author: Ashish
"""

sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];

def count_sheeps(sheep):
    count=0
    miss=['null','undefined']
    misscount=0

    for i in sheep:
        if i is False:
            count+=0
            continue
        elif i in miss:
            misscount+=1
        else:
            count+=1
    return count

print(count_sheeps(sheep))
    