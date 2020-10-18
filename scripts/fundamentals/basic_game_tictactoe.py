# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:04:40 2020

@author: Ashish
"""


def draw_board():
    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]
    print(row1)
    print(row2)
    print(row3)
    
def user_choice():
    
    # Will check if the user input is within a range and is a number
    
    # VARIABLES
    #acceptable_range = list(range(10))
    acceptable_range = range(0,10)
    within_range = False
    choice = "WRONG"
    
    # TWO CONFDITIONS TP CHECK
    # DIGIT OR WITHI RANGE== False
    
    while choice.isdigit()== False or within_range == False :
        
        choice = input("Please enter a number between 0-10: ")
        
        # DIGIT CHECK
        if choice.isdigit()==False:
            print("Sorry, that is not a digit!")
            
        # RANGE CHECK
        if choice.isdigit()== True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry! You are out of acceptable range")
                within_range = False
    
    return int(choice)
    
        

#draw_board()
user_choice()




# def user_choice():
#     '''
#     User inputs a number between 0-9 and we return this in 
#     integer form.
#     No parameter is passed when calling this function.

#     Returns
#     -------
#     None.

#     '''
#     choice = "wrong"
#     choice = input("Please enter a number (0-10):")
    
#     while choice.isdigit()== False:
#         choice = input("Enter a number (0-10): ")
    
#     return int(choice)
    
# #draw_board()
# choice= user_choice()
# print(choice)

