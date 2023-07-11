"""
Date: 12/24/2022
Miguel Ángel Bustamante Pérez

Min and max functions
"""

a_list = [58,96,72,24,35]
print(f'The highest value of the list is: {max(a_list)}')
print(f'The lowest value of the list is: {min(a_list)}')

names = ['Juan', 'Alicia', 'Pablo', 'Carlos']
print(f'The name that is more close to the start of the alphabet is: {min(names)}')

dic = {'C1':45, 'C2':11}
print(f'The lowest value inside the dictionary is: {min(dic.values())}')