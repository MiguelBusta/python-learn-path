"""
26/11/2022
Miguel Ángel Bustamante Pérez

Tuples
"""
my_tuple = (1, 2, (10, 20), 4)
print(f"Tuple: {my_tuple}")
print(f"Dataype: {type(my_tuple)}")

#Indexed
print(f"Value 0 of the tuple in pos 2 of the largest tuple {my_tuple[2][0]}")

# Casting
list_1 = list(my_tuple)
print(f"Changing tuple into list: {list_1}")

#Unpacking
a,b,c,d = my_tuple
print(c)

#count method
t = (1,2,3,1)
print(f"Counting the number of times that the value (parameter) is in the tuple: {t.count(1)}")
print(f"Index prints the index of the given element (parameter): {t.index(2)}")