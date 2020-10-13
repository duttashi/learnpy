# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:07:27 2020
Given a list of repeating numbers print the non-repeating numbers
@author: Ashish
"""

# declare a list of repeating and non-repating numbers
lst = [1,1,2,2,2,3,3,4,5,5,6]

# Solution #1
uniques = set(lst)
print("Solution #1")
print("set: ",uniques)
print("list: ", list(uniques))

# Solution #2
non_rep_nums = [] # declare an empty list
for item in lst:
    if (item not in non_rep_nums):
        non_rep_nums.append(item)
print("Solution #2")
print(non_rep_nums)

# Solution #3
from collections import Counter
cnt = Counter(lst)
print("Solution #3")
print([element for element in lst if cnt[element] == 1])