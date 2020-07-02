# -*- coding: utf-8 -*-
"""
# -*- coding: utf-8 -*-

Aim: To learn Object Oriented Programming in Python
Objective 1: Understand and practise Class, variable scope, 
constructors

Created on Mon Jun 22 08:10:09 2020

@author: Ashish
Reference book: Data Structures and Algorithms by Michael T. Goodrich
"""
class Flower:
    """ The flower class """
    def __init__(self, name, count):
        """ 
        Create a new flower instance 
        
        flower_name the name of flower (e.g. rose)
        flower_petal_count the number of petals in flower (e.g. 10)
        flower_price the price of flower (e.g. RM10)
        
        """
        # define constructors for initial value assignment
        self.__flower_name = name
        self.__flower_petal_count = count
        
        """ Note: a single leading underscore in the name of a data member, such as balance, implies that it is intended as nonpublic.
Users of a class should not directly access such members.
As a general rule, we will treat all data members as nonpublic. 
"""
        self._price = 0
        def set_flower_info(self, name, flower_type, petal_count, cost):
            self.__flower_name = name
            self.__flower_type = type
            self.__flower_petal_count = petal_count
            self.__flower_price = cost
            return
        
        """ Function/ Method Definitions for accessing flower data """
        def get_flower_info(self):
            """ Return flower details """
            return self._name
            
         
        
            
        

