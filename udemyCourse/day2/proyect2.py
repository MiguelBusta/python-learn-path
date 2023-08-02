"""
The sellers of a company receive 13% of their total sales. Your boss wants a program that computes the total comission for each employee acording to their sales. 

The program asks the name of the seller and how much did they sold during that month. 

The program will return a phrase that includes their name and how much money they earned. 
"""

def earned(name, com):
    """Function that prints the commission of the employee"""
    print(f"{name} will receive a commission of ${com}")


def main():
    """ Main function """
    #Variables 
    name = input("Write your name: ")
    sold = float(input("How much did you sold during this month?: "))

    #Compute of the 13% of commission
    com = round(sold * 0.13, 2)

    #Calls the function earned in order to print the final message
    earned(name, com)

main()