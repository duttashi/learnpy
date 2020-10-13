# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:20:05 2020

@author: Ashish
"""


friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

# --

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

print(user_movie in movies_watched)

# The `in` keyword works in most sequences like lists, tuples, and sets.