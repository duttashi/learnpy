# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:20:35 2020

Objective: Ask user for age and print the number of seconds they have lived for
@author: Ashish
"""
msg = "Hello! What is your age? : "
age_in_years = int(input(msg))

age_in_days = age_in_years * 365
age_in_hrs = age_in_days*24
age_in_mins = age_in_hrs*60
age_in_secs = age_in_mins * 60

print(f"You are {age_in_secs} seconds old!")

