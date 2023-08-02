"""
Date: 12/13/2022
Miguel Ángel Bustamante Pérez

Logical Operators 
"""

val_1 = (6 > 5) and (10 == 5*2)
print(val_1)

val_2 = (6 > 6) or (10 == 5*2)
print(val_2)

val_3 = (6 > 6) or not(10 == 5*2)
print(val_3)

text = "This is a brief phrase"
my_bool = ('phrase' in text) or ('python' in text)
print(my_bool)