"""
Date: 16/10/2023
Miguel Ángel Bustamante Pérez

* Exercise 3

TODO: Write a function that requires an undefined amount of arguments. This function will return True if in any moment the input value is a zero followed by a zero.

For example:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def enter_numbers(*args):
    """
    This function will return true if the input is equal to a zero followed by a zero
    """
    before_element = None
    for item in args:
        if before_element != None and before_element == 0:
            if item == 0:
                return True
        before_element = item
    return False

print(f"Test 1: {enter_numbers(5,6,1,0,0,9,3,5)}")
print(f"Test 2: {enter_numbers(6,0,5,1,0,3,0,1)}")
