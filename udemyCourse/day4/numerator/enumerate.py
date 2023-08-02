"""
Date: 12/22/2022
Miguel Ángel Bustamante Pérez

Enumerate function
"""

a_list = ['a', 'b', 'c']

#print each tuple
for item in enumerate(a_list):
    print(item)

#print each value with it's index 
for index, item in enumerate(a_list):
    print(index, item)

#Make a list of tuples 
list_of_tuples = list(enumerate(a_list))
print(list_of_tuples)