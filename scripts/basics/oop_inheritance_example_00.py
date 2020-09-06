# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:40:55 2020
Another Inheritance Example
@author: Ashish
"""
class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print '%s is eating %s' % (self.name, food)

class Dog(Animal):
    def fetch(self, thing):
        print "%s goes after %s" % (self.name, thing)
        
class Cat(Animal):
    def catchRats(self, thing):
        print "%s catches %s" % (self.name, thing)
        
d = Dog("Rover")
c = Cat("cindy")

d.fetch("ball")
c.catchRats("rats")



