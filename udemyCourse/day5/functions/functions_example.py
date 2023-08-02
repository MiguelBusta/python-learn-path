"""
Date: 01/16/2023
Miguel Ángel Bustamante Pérez

Functions Example
"""

coffee_prices = [('Cappuccino', 1.5), ('Expresso',2.5), ('Moka', 1.9)]

# for coffee, price in coffee_prices:
#     print(f'Coffee: {coffe}, Price: {price}')

def expensive_coffee(price_list):
    '''
    Function that is going to return the most expensive coffe.
    '''
    higher_price = 0
    more_expensive_coffee = ''

    for coffee, price in price_list:
        if price > higher_price:
            higher_price = price
            more_expensive_coffee = coffee
        else:
            pass
        
    return (more_expensive_coffee, higher_price)

coffe, price = expensive_coffee(coffee_prices)

print(f'The name of the most expensive coffee is: {coffe} and it\'s price is: {price}')