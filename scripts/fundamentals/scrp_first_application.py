# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:27:42 2020
Objective: Ask user its age and return the number of months
@author: Ashish
"""
user_age = int(input("What is your age: "))
age_in_months = user_age*12
age_in_weeks = age_in_months*48
age_in_days = age_in_months*30
age_in_hrs = age_in_days*24
age_in_mins = age_in_hrs*60
age_in_sec = age_in_mins*60
print(f"Your age is {user_age}")
print(f"\nYou are {age_in_months} months old!")
print(f"You are {age_in_weeks} weeks old!")
print(f"You are {age_in_days} days old!")
print(f"You are {age_in_hrs} hours old!")
print(f"You are {age_in_mins} minutes old!")
print(f"You are {age_in_sec} seconds old!")





