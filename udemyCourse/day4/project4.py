"""
Date: 12/25/2022
Miguel Ángel Bustamante Pérez

Project 4
"""

'''
The program must ask the user it's name, then it's going to tell him something like "Well, Juan, I've thinked a number between 1 and 100, you have only 8 tries to guess". Then in each try, the player must write a number and the program must answer four different things: 


1.- If the number is lower than 1 or larger than 100: "Not allowed value"
2.- If the number is lower than the selected one: "Wrong answer, that value is lower than the secret number". 
3.- If the number is bigger than the selected one: "Wrong answer, that value is bigger than the secret number".
4.- If the user guesses correctly: "You win, it took you X tries to guess the secret number". 
'''

from random import * #random library


def game(name):
    """
    Function that is going to make the loop for the game 
    """
    secret_n = randint(0,101)
    value = 0
    counter = 1

    print(f"Well, {name}, I have thinked a number between 1 and 100, you have only 8 tries to guess it.")

    while counter < 9:
        value = int(input('Enter a number: '))
        if value < 1 or value > 100:
            print('Not allowed value')
            counter += 1
        elif value < secret_n:
            print('Wrong answer, that value is lower than the secret number')
            counter += 1
        elif value > secret_n:
            print('Wrong answer, that value is bigger than the secret number')
            counter += 1
        elif value == secret_n:
            print(f'You win, it took you {counter} tries to guess the secret number')
            break
        else:
            print("Non valid expression")

    print('You lost')

def main():
    """
    Main function of the project
    """
    name = input("Please enter your name: ")
    game(name)

main()