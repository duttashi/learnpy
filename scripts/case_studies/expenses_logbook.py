# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:13:29 2020

@author: Ashish
"""

menu = """ Please select one of the followig options:
    1. Add a new entry
    2. View entries
    3. Exit
    
    Your selection: """
welcome = "Welcome to the expenses logbook!"

user_input = input(menu)

while(user_input := input(menu)) !="3":
    # deal with user input here
    if user_input =="1":
        print("Adding..")
    elif  user_input =="2":
        print("Viewing")
    else:
        print("Bye")
    user_input = input(menu)
