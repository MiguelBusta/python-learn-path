"""
Date: 01/16/2023
Miguel Ángel Bustamante Pérez

Dynamic Functions
"""

def check_3_digits(a_list):
    '''
    Function that checks if the given number is a 3 digit number. 
    '''
    list_3_digits = []

    for number in a_list:
        if number in range(100, 1000):
            list_3_digits.append(number)
        else:
            pass
    return list_3_digits


result = check_3_digits([555, 99, 600])
print(f'The result of the function is: {result}')