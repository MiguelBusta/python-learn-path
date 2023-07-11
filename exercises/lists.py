"""
En este programa se va a abarcar el tema de listas. 
"""

demo_list = [1, "hello", 1.34, True, [1, 2, 3]]

colors = ["red", "green", "blue"]

#constructor que nos permite crear una lista (es una función)
numbers_list = list((1,2,3,4)) #para agregar varios argumentos a la lista podemos usar la tupla (). 
print(numbers_list)
print(type(numbers_list))

#crear una lista basada en un rango 
r = list(range(1, 10)) #crea una lista del 1 al 10 de uno en uno
#range es un iterador que devuelve los valores de inicio, fin, paso (de cuanto en cuanto), no toca el último valor 
print(r) #imprime la lista del 1 al 9 

print(dir(colors)) #info de la lista 
