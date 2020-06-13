# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:15:36 2020
dictionary comprehension
@author: Ashish
"""
# A dictionary comprehension (DC) is similar to the list comprehension with following differences
# In DC, the brackets are curly braces {}
# In DC, the expression is in key:value format
print({x:x*x for x in range(10)})
