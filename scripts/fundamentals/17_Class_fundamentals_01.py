# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:15:14 2020

@author: Ashish

Objective: Class basics with __str()__ method
"""
# define a class

class Person:
    
    # Every class MUST have an init method to initialise the class variables
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    # define the string method
    def __str__(self):
        return "Hello"
    
    # the unambiguous method to recreate the class object
    def __repr__(self):
        return f"<Person({self.name}), {self.age})>"
# instantiate the class
bob = Person("Bib",56)
print(bob)
