# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:29:14 2020
Objective: Ask user country visited, then check if you have visited the ame country or not. if a match inform the user that you have also visted the same country

Program Flow:
    We'll create a variable that contains a list of countries.

    Then, we'll ask the user to enter a country name.

    We'll check if that name is inside our list, and if it is we'll tell the user we have also visited that country.

    If it's not inside our list, we'll tell the user we have not visited that country yet.
    
@author: Ashish
"""
my_country_list = ["Malaysia","India"]
msg = "enter the country name that you have visited? "
get_user_input = input(msg)

if get_user_input in my_country_list:
    print(f"I have visited {get_user_input} too!")
else:
    print(f"I have not visited {get_user_input}")

