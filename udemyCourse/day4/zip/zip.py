"""
Date: 12/22/2022
Miguel Ángel Bustamante Pérez

Zip function
"""

names = ['Ana', 'Hugo', 'Valeria']
ages = [65, 29, 42]
cities = ['Lima', 'Madrid', 'Mexico']

combined = list(zip(names,ages, cities))
print(combined)

for name, age, city in combined:
    print(f'{name}, has {age} years old and lives in {city}.')