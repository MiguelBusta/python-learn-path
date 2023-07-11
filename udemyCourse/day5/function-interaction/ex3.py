"""
Date: 01/18/2023
Miguel Ángel Bustamante Pérez

Function Interaction
"""

import random

def lanzar_moneda():
    '''
    Returns the obtained value after throwing a coin. It can return "Cara" or "Cruz" and has no arguments
    '''
    possible_values = ['Cara', 'Cruz']
    return random.choice(possible_values)

def probar_suerte(coin, lista_numeros):
    '''
    If coin == "Cara", then shows the message: "La lista se autodestruira" and empty the list. 
    IF coin == "Cruz" it must print: "La lista fue salvada" and return the list
    '''
    if coin == 'Cara':
        print('La lista se autodestruira')
        lista_numeros.clear()
        return lista_numeros
    elif coin == 'Cruz':
        print('La lista fue salvada')
        return lista_numeros

lista_numeros = [1,2,3,4,5]
coin = lanzar_moneda() #obtain the random value of the coin
print(f'Problem\'s result: {probar_suerte(coin, lista_numeros)}')