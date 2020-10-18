# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:41:59 2020
An example of multiple inheritance
Notes:
    1. Any class can inherit from multiple classes
    2. Python normally uses "depth-first" order,
    when searching inheriting classes.
    3. But when two classes inherit from the same class.
    4. Python eliminates the first mention of that class
    from the mro (method resolution call).
@author: Ashish
"""
class A(object):
    def dothis(self):
        print("Doing this in A")

class B(A):
    pass

class C(A):
    def dothis(self):
        print("Doing this in C")

class D(B,C):
    pass

# create class instance objects
d_instance = D()
d_instance.dothis()

print(D.mro())
