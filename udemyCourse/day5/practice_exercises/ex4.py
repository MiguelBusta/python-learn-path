"""
Date: 17/10/2023
Miguel Ángel Bustamante Pérez

* Exercise 4

TODO: Write a function called count_cousins() that requires one numeric argument only. This function will show all the odd numbers that exists within the range from zero to that number (included), and is going to return the amount of odd numbers that found.

Comments:
0 and 1 are not odd numbers
"""

def const_cousins(number):
    """
    TODO: This function will show all the odd numbers that exists from zero to the num value (included)
    """
    count_odd = 0
    odd_numbers = []
    is_prime = False

    for num in range(2, number+1):
        is_prime = True
        for i in range(2,num):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            # Update values
            odd_numbers.append(num)
            count_odd += 1
    print(f"The amount of odd numbers within the range is: {count_odd}")
    print(f"The list of odd numbers within that range is equal to: {odd_numbers}")

const_cousins(50)