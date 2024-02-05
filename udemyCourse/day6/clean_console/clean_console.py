"""
Date: 05/02/2024
Miguel Ángel Bustamante Pérez

* Directories

TODO: This program is only for educational purposes, in this case to learn how to clean the console within the code.

Comments:

"""

from os import system

name = input("Please enter your name: ")
age = input("Please enter your age: ")

# This executes the console command clear to clear the screen
system("clear")

print(f"This is your name: {name} and this is your age: {age}")