from cgi import print_arguments
from distutils.dep_util import newer_group
import random
from datetime import datetime
from Sudoku import check_box, check_number, print_grid, unsolved

grid = unsolved

#funcion para solucionar el sudoku
def solve_sudoku(grid):
    new_grid = []
    numbers = range(0,10) # lista de numeros
    row = 0
    while row < 9:
        col = 0
        temp_row = grid[row]
        while col < 9:
            if grid[row][col] == 0:
                unused_numbers = list(set(numbers) ^ set([grid[x][col] for x in range(9)] + grid[row] + check_box(grid,row,col))) ###
                if len(unused_numbers) < 1:
                    grid[row] = temp_row
                    break
                else:
                    number = random.choice(unused_numbers)
                    if check_number(grid,row,col,number):
                        grid[row][col] = number
                        col += 1
            else:
                col += 1
        row += 1

    return new_grid


solved = solve_sudoku(grid)

print_grid(solved)