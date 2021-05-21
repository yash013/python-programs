# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:36:32 2020

@author: This Pc
"""

import random
randomNum = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess!=randomNum):
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if(userGuess==randomNum):
        print("You guessed it right!")
    else:
        if(userGuess>randomNum):
            print("You guessed it wrong!Enter a smaller number")
        else:
            print("you guessed it wrong!Enter a larger number")
            
print(f"You guessed the number in {guesses} guesses")
