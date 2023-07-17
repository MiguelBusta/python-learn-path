"""
Date: 16/10/2023
Miguel Ángel Bustamante Pérez

* Exercise 4

TODO: Write a function called count_cousins() that requires one numeric argument only. This function will show all the odd numbers that exists within the range from zero to that number (included), and is going to return the amount of odd numbers that found.

Comments:
0 and 1 are not odd numbers
"""

def const_cousins(num):
    """
    TODO: This function will show all the odd numbers that exists from zero to the num value (included)
    """
    count_odd = 0
    odd_numbers = []
    for i in range(0, num+1 ,1):
        if i%2 != 0 and i != 0 and i != 1:
            odd_numbers.append(i)
            count_odd += 1
    print(f"The amount of odd numbers within the range is: {count_odd}")
    print(f"The list of odd numbers within that range is equal to: {odd_numbers}")

const_cousins(5)