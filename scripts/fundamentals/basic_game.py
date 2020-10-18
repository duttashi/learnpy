# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:38:20 2020
Objective: create a basic game to practice python input and decision control statements
@author: Ashish
"""
# required libraries
from sys import exit
# global vars
health=10
print("Welcome to my game")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Welcome ", name, "You are ",age, " years old!")
if (age<18):
    print("You are juvenile and cannot play this game")
    exit()
elif (age>=18):
    print(name, "lets play the game")
    answer = input("Do you want to play? ")
    if (answer == "yes" or answer == "YES" or answer == "Yes" or answer == "y" or answer=='yes'):
        print("You are starting with 10 health")
        print("Lets play...")
        print("First choice... (left/right): ")
        choice = input()
        if(choice=='left'):
            choice = input("Nice... you follow a path a reach a lake..."
                           " Do you swim or walk around (swim/walk)?: ")
            if(choice=='swim'):
                print("Argh... a crocodile bit your leg. You loose 5 points")
                health-=5
                if(health>=5):
                    print("Your health is ",health)
                    print("Hooray! You have won the game")
                else:
                    print("Your health is ", health, "low and you've lost the game")
                    exit()
        #continue
            else:
                print("Argh... a snake bit your leg.. You loose 10 points")
                health-=10
                if (health<5):
                    print("Your health is ", health)
                    print(name, "You have lost the game, try again!")
                    exit()
        else:
            choice = input("Nice... you see a mountain... Do you climb it or dig it (climb/dig)?: ")
            if(choice=='climb'):
                print("Argh... you sprained your leg. You loose 5 points")
                health-=5
            else:
                print("Your nuts! you cant dig a mountain... You loose 10 points")
                health-=10
                
                if(health<5):
                    print("Your health is ",health)
                    print("You have lost the game")
                    exit()
        
        choice = input("Second choice... (love/hate)?: ")
        if(choice == 'love'):
            choice = input("Nice... you see a princess by the lake. What do you do (talk/walk away)? ")
            if(choice == "talk"):
                print("The princess invites you to meet her parents")
                health+=10
                print("Yay... you scored. Your current health is: ", health)
            else:
                print("Sad, the princess could have helped you progress")
                print("You loose 10 points")
                health-=10
                if(health==0):
                    print("You lost the game. Your health is: ", health)
        else:
            choice = input("Nice... you see a an evil king kidnap the princess and ride away. What do you do (fight/run)? ")
            if(choice == "fight"):
                print("You saved the princess. She invites you to meet her parents")
                health+=20
                print("Yay... you scored. Your current health is: ", health)
            else:
                print("Your a coward")
                print("You loose 10 points")
                health-=10
                if(health==0):
                    print("You lost the game. Your health is: ", health)
                    exit()
            
                
                
    else:
        exit()
else:
    print("please enter age in numbers only")
    
