print("This script is meant to be at least 30 lines long so that i do not get less marks in lab1")

from functools import lru_cache

def isSafe(num:int,x:int,y:int,sudoku:list):
    '''Function to check whether or not the current block is safe or not..'''

    # check teh 3x3 box
    cornerx = ( x // 3 ) * 3
    cornery = ( y // 3 ) * 3

    for i in range(cornerx,cornerx+3):
        for j in range(cornery,cornery+3):
            if sudoku[i][j] == num:
                return False

    for i in range(9):
        if(sudoku[i][y] == num or sudoku[x][j] == num):
            return False

    return True


# @lru_cache  Note that lru cahce cannot hash the mutable objects like list so either you need to first convert the list to tuple
def solveSudoku(sudoku):
    '''Tries all the combinations'''
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j] == 0):
                for num in range(1,10):
                    if isSafe(num,i,j,sudoku):
                        sudoku[i][j] = num
                        if solveSudoku(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return True






# remove thie line jsut ot correct eh syntax
def printSudoku(sudoku):
    '''Prints the Sudoku board.'''
    for row in sudoku:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("\nOriginal Sudoku:")
printSudoku(sudoku)

if solveSudoku(sudoku):
    print("\nSolved Sudoku:")
    printSudoku(sudoku)
else:
    print("No solution exists.")


