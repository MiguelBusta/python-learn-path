"""
Date: 07/10/2023
Miguel Ángel Bustamante Pérez

Undefined Arguments **kwargs
"""

def add(**kwargs):
    total = 0
    print(type(kwargs)) #This is a dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        total += value

    return total

print(add(x=3, y=5, z=2))