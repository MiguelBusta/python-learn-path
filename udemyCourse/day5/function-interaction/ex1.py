"""
Date: 01/18/2023
Miguel Ángel Bustamante Pérez

Function Interaction
"""

import random

def lanzar_dados():
    '''
    Throw two dices and return the result
    '''
    res1 = random.randint(1,6)
    res2 = random.randint(1,6)
    
    return res1, res2
    
def evaluar_jugada(val1, val2):
    '''
    Function that receives the result of throwing the dices and return
    a message without printing that contain the sum of those values 
    '''
    suma_dados = val1 + val2
    
    if suma_dados <= 6: 
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (suma_dados > 6) and (suma_dados < 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

val1, val2 = lanzar_dados()
print(evaluar_jugada(val1, val2))