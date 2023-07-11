"""
Date: 07/10/2023
Miguel Ángel Bustamante Pérez

Undefined Arguments summary
"""

def test(num1, num2, *args, **kwargs):
    print(f'The first value is {num1}')
    print(f'The second value is {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for key, value in kwargs.items():
        print(f'{key} = {value}')


test(15, 50, 100, 200, 300, 400, x = 'one', y = 'two', z = 'three')