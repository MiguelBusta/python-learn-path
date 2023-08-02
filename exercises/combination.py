"""
You are in charge of the cake for a child’s birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
Example

Candles = [4,3,2,4]


The maximum height candles are 4 units high. There are 2 of them, so return 2.
"""

def check_cake(counter, candles):
    high_candle = max(candles)
    for i in candles:
        if high_candle == i: 
            counter += 1
    return counter

def c_cake(counter,candles):
    max_number = 0
    for i in range(len(candles)):
        if candles[i] > max_number: 
            max_number = candles[i]
            counter = 1
        elif candles[i] == max_number: 
            counter += 1
    return counter

def main(): 
    counter = 0
    candles = [4, 3, 2, 4, 5]
    total = c_cake(counter, candles)
    print(total)

main()