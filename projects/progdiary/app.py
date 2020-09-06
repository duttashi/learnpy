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

def prompt_user_input():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    create_table()
    add_entry(entry_content, entry_date)

print(welcome)
# Looping while asking user for input

while(user_input := input(menu)) != "3":
    
    if user_input=="1":
        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")
        
        add_entry(entry_content, entry_date)
    elif user_input == "2":
        for entry in get_entries():
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Invalid option, please try again!")
        
            
        


    
