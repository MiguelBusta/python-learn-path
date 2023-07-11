"""
Date: 07/10/2023
Miguel Ángel Bustamante Pérez

Exercise 1

Create a function called return_distinct() that receives 3 integers as parameters.

If the sum of the 3 numbers is higher than 15, is going to return the highest number.

If the sum of the 3 numbers is lower than 10, return the lowest number.

If the sum of the three numbers is a value between 10 and 15 (included) it is going to return the intermediate value.
"""

def return_distinct(*numbers):
    if (sum(numbers) > 15):
        return max(numbers)
    elif(sum(numbers) < 10):
        return min(numbers)
    else:
        max_num = max(numbers)
        min_num = min(numbers)
        mid_num = sum(numbers) - (max_num + min_num)
        return mid_num

print(return_distinct(3,4,8))