# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:57:46 2020
On Lists, typles and Sets
A list is defined by square brackets. The list components are separated by comma
Modifications of elements i list is possible.
A tuple is defined by round brackets (). A tuple element canot be modified.
A set cannot have duplicates. Accessing elements using subscript notation is not allowed in sets.
A dictionary is defined by curly brackets

@author: Ashish
"""
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

l[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Add to a list by using `.append`

l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets can't have the same element twice.

s.add("Bob")
print(s)


