"""
Created on Tue Oct  6 15:29:11 2020.
Problem source: codewars.com
The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should
return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
@author: Ashish
"""
def powerset(s):
    # function that accepts a list and print its sets
    x = len(s)
    for i in range(1, 1<<x):
        print ([s[j] for j in range(x) if (i & (1 << j))])
        
# test case
# ensure to pass a list
powerset([4,5,6])