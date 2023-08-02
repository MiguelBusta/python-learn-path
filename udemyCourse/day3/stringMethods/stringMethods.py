"""
06/10/2022
Miguel Ángel Bustamante Pérez

String Methods
"""

from tkinter import E


text = "This is Federico's text"

#Using the upper method
print(text.upper())

#Using the lower method
print(text.lower())

#Using split
print(text.split())
print(text.split("i"))

#Using join method
a = "Hello,"
b = "my"
c = "name"
d = "is"
e = "Mario"
#Joins the elements from the list using the space as separator
f = " ".join([a,b,c,d,e])
print(f)

#Using the find method
print(text.find("text"))
print(text.find("link"))

#Using replace method
print(text.replace("Federico's", "Miguel's"))
#You can also concatenate this method
print(text.replace("Federico's", "Miguel's").replace("text", "phone"))