"""
Date: 08/10/2023
Miguel Ángel Bustamante Pérez

Exercise 2

Write a function that receives any word as parameter, and return all it's
unique letters (without repeats) but in alphabetic order.

For example, if we give the word 'entretenido', it should return ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""

def obtain_unique_letters(word):
    '''Function to only obtain each letter of a word without repeats in alphabetic order'''
    unique_letters = []
    for letter in word:
        if len(unique_letters) == 0:
            unique_letters.append(letter)
        elif letter not in unique_letters:
            unique_letters.append(letter)
        else:
            continue
    unique_letters.sort()
    return unique_letters

print(obtain_unique_letters('entertainment'))