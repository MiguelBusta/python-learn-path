"""
Date: 12/15/2022
Miguel Ángel Bustamante Pérez

While Loops
"""

coins = 5

while coins > 0:
    print(f"I have: {coins} coins")
    coins -= 1
else:
    print("I have no more money")


answer = 's'

while answer == 's':
    answer = input("Do wou want to continue? (s/n)")
else:
    print("Thanks!!!")