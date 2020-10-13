# -*- coding: utf-8 -*-
"""
Inheritance example
Created on Thu Aug 20 12:33:56 2020

@author: Ashish
"""

class Date():
    def get_date(self):
        return "2020-8-20"
    
class Time(Date):
    def get_time(self):
        return "10 am"

# create object
dt = Date()
print(dt.get_date())

tim = Time()
print(tim.get_time())
print(tim.get_date())
