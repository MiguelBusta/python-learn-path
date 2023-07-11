"""
Date: 01/18/2023
Miguel Ángel Bustamante Pérez

Function Interaction
"""

def reducir_lista(lista_numeros):
    '''
    return the given list without duplicates and deleting the highest value, 
    the order of the elements can be modified
    '''
    lista_xd = []
    [lista_xd.append(n) for n in lista_numeros if n not in lista_xd]
    lista_xd.sort()
    lista_xd.pop()

    lista_numeros = lista_xd
    return lista_numeros


def promedio(lista_numeros):
    '''
    Function that returns the average of the values inside a list
    '''
    return sum(lista_numeros) / len(lista_numeros)

lista_numeros = reducir_lista([1, 1, 5, 3, 6, 3, 5, 6, 1,17,17,20])
print(lista_numeros)
print(promedio(lista_numeros))