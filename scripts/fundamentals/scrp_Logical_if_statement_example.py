# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:22:18 2020
@author: Ashish
Objective: Calculate the body mass index (BMI) of a person
Input: weight, height
output: bmi and classification
if bmi less than equal to 18.5, classification- underweight
Greater than 18.5 or less tha equal to 24.9, classification- Normal weight
Greater than 24.5 or less tha equal to 29.9, classification- Over weight
Greater than or equal to 30, classification- Obesity

Formula BMI = weight/(height*height)
"""
user_choice = "y"

while(user_choice!="n"):

    print("Body Mass Index Calculator")
    print("---------------------------")

    weight = float(input("Enter your current weight in Kg (e.g. 75.5): "))
    height = float(input("Enter your height in feet (e.g. 1.70): "))
    bmi = round( (weight/(height**2)), 2)

    if(bmi<=18.5):
        classification = "Underweight"
    elif(bmi>18.5 and bmi<=24.9):
        classification = "Normal weight"
    elif(bmi>24.9 and bmi<=29.9):
        classification = "Over weight"
    elif(bmi>=30):
        classification = "Obese"
    else:
        classification ="Invalid"
    print("Your current BMI is: %.2f" % bmi, "and your",classification)

    user_choice = input("Do you want to check BMI again (y/n):")

    



