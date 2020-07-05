# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:04:40 2020

@author: Ashish
"""


def draw_board():
    horiz_line = "-"
    verti_line = "|"
    cross = "X"
    circle = "0"
    print(horiz_line*10)
    print(cross*2)
    print(verti_line*10)
    
def user_choice():
    '''
    User inputs a number between 0-9 and we return this in 
    integer form.
    No parameter is passed when calling this function.

    Returns
    -------
    None.

    '''
    choice = "wrong"
    choice = input("Please enter a number (0-10):")
    
    while choice.isdigit()== False:
        choice = input("Enter a number (0-10): ")
    
    return int(choice)
    
#draw_board()
choice= user_choice()
print(choice)

