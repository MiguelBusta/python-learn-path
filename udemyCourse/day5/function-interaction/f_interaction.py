"""
Date: 01/16/2023
Miguel Ángel Bustamante Pérez

Function Interaction
"""
from random import shuffle #import the random module to use the shuffle method

# Initial List
sticks = ['-', '--', '---', '----']

# Shuffle sticks
def shuffle_sticks(sticks):
    '''
    Function that will receive a list with sticks and will shuffle it
    '''
    shuffle(sticks) #shuffle the sticks inside the list
    return sticks

# Ask for the first try
def test_luck():
    '''
    Ask the user to enter a number from 1 to 4
    '''
    try_number = ''

    while try_number not in ['1', '2', '3', '4']:
        try_number = input('Choose a number from 1 to 4: ')
    
    return int(try_number)

# Check try
def check_try(sticks, user_try):
    if sticks[user_try - 1] == '-':
        print('You have to wash the dishes :c')
    else:
        print('This time you were lucky!!!')
    print(f'The stick choosed was: {sticks[user_try-1]}')


new_sticks = shuffle_sticks(sticks) #shuffle the sticks
selection = test_luck() #choose a number
check_try(new_sticks, selection) #finding which stick you choose
