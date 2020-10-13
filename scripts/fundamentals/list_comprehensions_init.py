# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:44:11 2020

@author: Ashish
"""


x = int ( input("Enter a number: ")) 
y = int ( input("Enter a number: ")) 
n = int ( input("Enter a number: ")) 
print ([[ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])