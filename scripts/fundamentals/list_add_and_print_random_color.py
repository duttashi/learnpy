# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 08:43:59 2020
Objective: Create a guess game with the name of the colors. At each
round pick a random color from a list and let the user try to guess
it. Whaen he does it, ask if he wants to play again. Keep playing
until the user types no

@author: Ashish
"""

# declare variables
colors_list = ['red','blue','green','black']
resp = 'yes'

print("Guess the color")
while resp:
    color_choice = input("Enter the color name: ")
    if (color_choice in colors_list):
        print("You got it")
        
        break
    else:
        print("Sorry! wrong choice")
        print("Do you want to try again?")
        resp = input("Enter choice (yes/no): ")
        if (resp=="no"):
            print("Goodbye!")
            break
        # while (resp!="no"):
        #     continue
        
        

