# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:32:21 2020

@author: Ashish
"""
# importing functions from another python file
from database import add_entry, get_entries, create_table, close_connection

# Declare variables
menu = """ Please select one of the following options:
    1) Add new entry for today
    2) View entries
    3) Exit
    
    Your selection: """

welcome = "Welcome to the programming diary!"

print(welcome)
# Looping while asking user for input
user_input = int(input(menu))

def prompt_user_input():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    create_table()
    add_entry(entry_content, entry_date)
    
while(user_input!=3):
    # We'll deal with user input here
    if user_input == 1:
        #print("Adding...")
        prompt_user_input()
    elif user_input == 2:
        #print("Viewing...")
        #view_entries(entries)
        get_entries()
    else:
        print("Invalid option! please try again")
        close_connection()
        
    user_input = int(input(menu))