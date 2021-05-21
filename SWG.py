# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:02:32 2020

@author: This Pc
"""

print("Welcome to Snake, Water, Gun game\n")

import random
attempts = 1
comp_points = 0
your_points = 0
while (attempts<=10):

    y = ["Snake", "Water", "Gun"]
    z = random.choice(y)
    print("Enter your choise(Snake, Water, Gun)")
    inp = input()
    
    if (z == inp):
        print("tie")
        print("no one gets point\n")
        
    elif(z == "Snake" and inp == "Water"):
        comp_points = comp_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The snake drank water\n")
        print("You lost this round")
        print("computer get 1 point\n")
        
    elif(z == "Snake" and inp == "Gun"):
        your_points = your_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The snake was shoot and he died\n")
        print("You won this round")
        print("you get 1 point\n")
        
    elif(z == "Water" and inp == "Snake"):
        your_points = your_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The Snake drank Water\n")
        print("You won this round")
        print("you get 1 point\n")
        
    elif(z == "Water" and inp == "Gun"):
        comp_points = comp_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The gun sake in water\n")
        print("You lost this round")
        print("computer get 1 point\n")
        
    elif(z == "Gun" and inp == "Snake"):
        comp_points = comp_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The snake was shoot and snake died\n")
        print("You won this round")
        print("computer get 1 point\n")
        
    elif(z == "Gun" and inp == "Water"):
        your_points = your_points + 1
        print(f"you choosed {inp} and computer guess is {z}")
        print("The gun sake in water\n")
        print("You won this round")
        print("you get 1 point\n")
        
    else:
        print("Invalid Input")
        
        
    print(10 - attempts, "no of attempts left")
    attempts = attempts + 1
    
    if attempts>10:
        print("Game Over")
        
if comp_points > your_points:
    print("You loose")
    
else:
    print("You Win")
    
print(f"your points is {your_points} and computer points is {comp_points}.")
        
        

   