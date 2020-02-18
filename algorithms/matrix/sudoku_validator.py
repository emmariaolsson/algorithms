"""
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

(More info at: http://en.wikipedia.org/wiki/Sudoku)
"""

# Using dict/hash-table
from collections import defaultdict
branches = [0]*14
def valid_solution_hashtable(board):
    for i in range(len(board)):
        branches[0] = 1
        dict_row = defaultdict(int)
        dict_col = defaultdict(int)
        for j in range(len(board[0])):
            branches[1] = 1
            value_row = board[i][j]
            value_col = board[j][i]
            if not value_row:
                #Not covered
                branches[2] = 1 
                print(branches)
                return False
            elif value_col == 0:
                branches[3] = 1
                print(branches)
                return False
            elif value_row in dict_row:
                #Not covered
                branches[4] = 1
                print(branches)
                return False
            else:
                branches[5] = 1
                dict_row[value_row] += 1

            if value_col in dict_col:
                #Not covered
                branches[6] = 1
                print(branches)
                return False
            else:
                branches[7] = 1
                dict_col[value_col] += 1

    for i in range(3):
        branches[8] = 1
        for j in range(3):
            branches[9] = 1
            grid_add = 0
            for k in range(3):
                branches[10] = 1
                for l in range(3):
                    branches[11] = 1
                    grid_add += board[i*3+k][j*3+l]
            if grid_add != 45:
                #Not covered
                branches[12] = 1
                print(branches)
                return False
            else:
                branches[13] = 1
    print(branches)
    return True
