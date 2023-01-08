""""
Situación Problema

Realizar un programa que genere un tablero de ajedrez que coloque 8 reinas, las cuales dependiendo de su posición deben de estar libres para moverse, es decir, no deben apuntar hacia ninguna otra reina.

Utilizando divide and conquer 
""" 

#Global variables

#number of queens 
n = 8 

def print_solution(board):
    """ A utility function to print solution """
    for i in range(board):
        for j in range(board):
            print(board[i][j], end = " ")
        print() 


def eightQueen(board, col):
    """
    Recursive function to find all the possible combinations for the queens in order to not eat each other.
    """

    """
    Base case: 
    If all queens are placed then return True
    """
    if(col >= n):
        return True

def main():
    """
    Main function

    This function will contain the main variables to solve de N Queen Problem using backtracking.

    Backtracking algorithmic technique is used to solve problems recursively by trying to build a solution incrementally, one piece at a time. 
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    if eightQueen(board, 0) == False: 
        print("There is no solution")
    else: 
        print_solution(board)

main()