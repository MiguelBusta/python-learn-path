"""
Date: 12/25/2022
Miguel Ángel Bustamante Pérez

List comprehension
"""

word = 'Python'

#Normal form to make this
# a_list = []
# for letter in word:
#     a_list.append(letter)

#Using list comprehension is way better 
a_list = [letter for letter in word]
print(a_list)

#more examples
list_n = [number for number in range(0, 21, 2)]
print(f'A list with only even numbers: {list_n}')

list_n = [number for number in range(0, 21, 2) if number * 2 > 10]
print(f'A list with only even numbers that multiplied by 2 are bigger than 10: {list_n}')

list_n = [number if number * 2 > 10 else 'no'for number in range(0, 21, 2)]
print(f'A list with even numbers that multiplied by 2 are bigger than 10 and also the ones that are not are replaced with \'no\': {list_n}')

ft = [10,20,30,40,50]
mts = [number*3.281 for number in ft]
print(f'Values in fts: {ft}')
print(f'Values in mts: {mts}')