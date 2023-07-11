# Tipos de datos 

# Strings 
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')

print(type("Hola")) #La función type te regresa el tipo de dato que este adentro de los paréntesis 

# Operaciones con strings 
print("Bye" + " World") #Se pueden concatenar strings con el operador suma

# Numeros 
print(30)
print(type(30)) #tipo de dato int (entero)
print(30.5)
print(type(30.5)) #tipo de dato float (flotante)

# Boolean datatypes
print(True)
print(type(True))
print(False)
print(type(False))

"""
List
Lista de datos, pueden ser de un mismo tipo de datos o bien de una combinación de varios tipos de datos  
"""
print([10,20,30,40])
print(["Hello","Bye"])
print([10,True,30,"XD"])
print([]) #lista vacia

#Tuples: tuplas, similares a las listas en el sentido de que agrupan datos, solo que esta no es modificable (inmutable)
print((10,20,30,55))
print(()) #tupla vacia 

#Dictionaries: agrupar datos que pertenecen a una misma entidad
{
    #key      #value
    "nombre":"Jefe Maestro", 
    "apellido": "117",           
    "apodo":"Demonio"
}      
#cada elemento del diccionario esta definido por un nombre y un valor.
# Otro ejemplo:  
print(type({
    "Latitud":1234,
    "Longitud": 5677
}))

#tipo de dato que no tiene nada 
None #decirle que lo que vamos a utilizar no esta definido como un tipo de dato 
print(type(None))




