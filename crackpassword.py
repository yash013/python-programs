import random
import string
import pyautogui

# chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars = string.printable
char_list = list(chars)

password = pyautogui.password("Enter your password : ")

guess_password = ""

while (guess_password != password):
    guess_password = random.choices(char_list,k=len(password))

    print("<=============" +str(guess_password)+ "=============>")

    if(guess_password == list(password)):
        print("Your password is:"+ "".join(guess_password))
        break
