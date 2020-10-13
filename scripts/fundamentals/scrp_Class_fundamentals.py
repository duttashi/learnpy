# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:15:14 2020

@author: Ashish

Objective: Class basics
"""
# define a class

class Student:
    
    # Every class MUST have an init method to initialise the class variables
    def __init__(self):
        self.name = "Ashish"
        self.grades = (10,20,30,40)
        
        
    # define another method
    def average_grades(self):
        return sum(self.grades)/len(self.grades)
        
# instantiate the class
student = Student()
print(student.name)
print(student.grades)
print(student.average_grades())

