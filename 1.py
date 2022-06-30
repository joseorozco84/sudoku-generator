import random

# nums = [1,2,3,4,5,6,7,8,9]
# random.sample(range(1,10),9)
# grid = [[random.randrange(1,10) for x in range(9)] for y in range(9)]

# funcion para pintar la grilla
def printgrid(grid):
    TableTB = "+--------------------------------+"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)


# funcion para llenar la grilla con valores validos
def valid_grid(grid):
    for row in range(9): #itera sobre las filas
        numbers = range(1,10)
        while 0 in grid[row]: #mientras haya un 0 en la fila hacer loop
            for col in range(9): #itera sobre las columnas
                number = random.choice(numbers) #elige numero al azar del 1 al 10
                if (number not in grid[row]) and (number not in column(grid,col)) and (number not in box(grid,row,col)): #si el numero no esta en la fila ni en la columna
                    grid[row][col] = number #agrega el numero a la columna
    

def box(grid,row,col):
    box = []
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for x in range(row_start, row_start + 3):
        for y in range(col_start, col_start + 3):
            box.append(grid[x][y])

    return box


# funcion para generar una grilla vacia
def grid():
    grid = []
    column = []
    #completa la grilla con 0
    for _ in range(9):
        grid.append([0 for x in range(9)])
        column.append(grid[_][0])

    valid_grid(grid)

    column = [grid[x][0] for x in range(9)]
    
    delete_random(grid,30) #borra aleatoriamente de la grilla la cantidad de numeros

    # solve_sudoku(grid)


    print(f'\nGRID: {grid}\n')
    # print(f'Fila 0: {row}')
    # print(f'Columna 0: {column}')

    return grid

# funcion para generar una linea random del 1 al 9
def random_row():
    row = []
    row.extend(random.sample(range(1,10),9))
    return row

# funcion para mostrar columna
def column(grid,col):
    for _ in range(9):
        column = [grid[x][col] for x in range(9)]
    return column

# funcion para quitar numeros aleatorios
def delete_random(grid,qty):
    for _ in range(qty):
        row = random.choice(range(9))
        col = random.choice(range(9))
        while grid[row][col] == 0:
            row = random.choice(range(9))
            col = random.choice(range(9))
        else:
            grid[row][col] = 0
    return grid

#funcion para solucionar el sudoku
def solve_sudoku(grid):
    solved = []
    for row in range(9):
        while ('-' in grid[row]) or (0 in grid[row]):
            for col in range(9):
                number = random.choice(range(1,10))
                if number not in box(grid,row,col):
                    if number not in grid[row] and number not in column(grid,col):
                        grid[row][col] = number
                        solved.append(number)
    
    print(solved)

printgrid(grid())


