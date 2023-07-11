"""
08/12/2022
Miguel Ángel Bustamante Pérez

Sets
"""

"""
First way of declaring sets 
my_set = set([1, 2, 3, 4, 5])
print(type(my_set))
print(my_set)

Recomended way to declare sets
another_set = {1, 2, 3}
print(type(another_set))
print(another_set)

"""

#sets don't accept lists or diccionaries but they accept tuples because they're immutable
set_1 = {1, 2, (3, 4)}
print(f"Set 1: {set_1}")
#len() function is available for sets
print(f"Length of set 1: {len(set_1)}")

set_2 = {2,6,7}
print(f"Set 2: {set_2}")

set_3 = set_1.union(set_2)
print(f"Set that is the union of set 1 and set 2: {set_3}")