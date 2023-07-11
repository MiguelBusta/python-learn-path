"""
Date: 12/24/2022
Miguel Ángel Bustamante Pérez

Random
"""

from random import * #import all the methods from the library
 
#Use of randint()
random_num = randint(1,50)
print(f'Using randint() function: {random_num}')

#Use of uniform()
random_uniform = round(uniform(1,5),1)
print(f'Generate a random float value with one decimal: {random_uniform}')

#Use of random()
zero_one = round(random(),2)
print(f'Prints a random decimal number from 0 to 1: {zero_one}')

#Use of choice()
colors = ['blue', 'red', 'green', 'yellow']
random_color = choice(colors)
print(f'Selecting a random element from the iterable object: {random_color}')

#Use of shuffle()
numbers = list(range(5,50,5)) #making a list that increases 5 by 5
print(f'List without shuffle: {numbers}') 
shuffle(numbers)
print(f'List with shuffle: {numbers}')