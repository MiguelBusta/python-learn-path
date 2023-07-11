"""
10/10/2022
Miguel Ángel Bustamante Pérez

Dictionaries
"""
#Sort of real life example using dictionaries
client = {
    'name':'Michael',
    'lastname':'Bustamante',
    'weight':65,
    'height':1.91
}

consult = (client['lastname'])
print(consult)

#Dictionary with a list and a dictionary inside of it. 
dic = {
    'c1':55, 
    'c2':[10,20,30],
    'c3':{
        's1':'xd',
        's2':0.5
    }
}
#Accesing the value with index 1 inside the list
print(dic['c2'][1])
#Accesing a dictionary inside of another dictionary
print(dic['c3']['s1'])

#Exercise
#Print the character 'e' but in uppercase 
dic2 = {
    'c1':['a','b','c'], 
    'c2':['d','e','f']
}
#Accesing the letter e of the list that is inside the dictionary and with the upper method turning it into uppercase
print((dic2['c2'][1]).upper())

dic3 = {
    1:'a',
    2:'b'
}

#Adding a new pair
dic3[3] = 'c'
#Overwrite 
dic3[2] = 'B'

print(dic3)

#printing only keys
print(dic3.keys())
#printing only values
print(dic3.values())
#printing all items inside a dictionary
print(dic3.items())