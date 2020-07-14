# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:15:05 2020
Logical condition: If statement
@author: Ashish
"""
day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")

# -- Problem: user not entering what we expect --

day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")


