# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:13:53 2020
Booleans
@author: Ashish
"""


# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False