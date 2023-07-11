"""
Date: 01/18/2023
Miguel Ángel Bustamante Pérez

Undefined Arguments
"""

def suma_cuadrados(*args):

    total = 0

    for num in args:
        total += num**2

    return total