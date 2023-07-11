"""
Date: 12/14/2022
Miguel Ángel Bustamante Pérez

For Loops
"""


# Iterate through a list
names = ["Juan", "Ana", "Carlos", "Belen", "Fran"]
for i in names:
	print(i)

# Iterate through a list of lists
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

# Iterate through a dictionary
dic = {'key1': 'a', 'key2': 'b', 'key3': 'c', 'key4': 'd'}

# Iterate through the keys
for item in dic:
    print(item)

# Iterate through the tuples
for item in dic.items():
    print(item)

# Iterate through the values
for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)

for letter in "federico":
    if letter == 'r':
        continue
    else:
        print(letter)