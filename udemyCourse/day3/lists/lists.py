"""
07/10/2022
Miguel Ángel Bustamante Pérez

Lists 
"""

#Lists concatenation
print("\nlists concatenation")
myList1 = ["a", "b", "c"]
myList2 = ["d", "e", "f"]
print(myList1 + myList2)

#Lists modification 
print("\nlists modification")
myList3 = myList1 + myList2
myList3[0] = 1
print(myList3)

#Append method
print("\nAppend method")
myList3.append("z")
print(myList3)

#Pop method
print("\nPop method")
save = myList3.pop()
print(myList3)
print(f"The popped element is {save}")

#Ordering elements inside a list
print("\nOrdering elements")
anotherList = ["g", "o", "b", "m", "c"]
anotherList.sort()
print(anotherList)

#Reversing elements inside a list 
print("\nReversing elements")
aList = ["g", "o", "b", "m", "c"]
aList.reverse()
print(aList)