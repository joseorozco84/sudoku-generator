import random
from datetime import datetime


start_time = datetime.now()

# funcion para pintar la grilla [grid] en consola
def print_grid(grid):
    grid_tb = "+--------------------------------+"
    grid_mb = "|----------+----------+----------|"
    print(grid_tb)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(grid_mb)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(grid_tb)

class Sudoku_generator:

    def __init__(self): # constructor con atributos comunes
        self.grid = []
        self.size = 9
        self.content = [0,1,2,3,4,5,6,7,8,9]
        [self.grid.append([0 for x in range(self.size)]) for n in range(self.size)]

    def __str__(self): # metodo para imprimir caracteristicas
        return (f'Size: {self.size} x {self.size}, Content: {self.grid}')

    # metodo para devolver el cuadrante segun la posicion
    def check_box(self,grid,row,col):
        box = []
        row_start = (row // 3) * 3 # inicio de la fila del cuadrante
        col_start = (col // 3) * 3 # inicio de la columna del cuadrante
        # loop de cuadrante 3 x 3
        for x in range(row_start, row_start + 3):
            for y in range(col_start, col_start + 3):
                box.append(grid[x][y]) # apenda todos los numeros del cuadrante
        return box

    # metodo para devolver True si la posicion del numero es valida 
    # # chequea fila, columna y cuadrante
    def check_number(self,grid,row,col,number):
        box = []
        column = [grid[x][col] for x in range(9)] # columna segun posicion
        row_start = (row // 3) * 3 # inicio de la fila del cuadrante
        col_start = (col // 3) * 3 # inicio de la columna del cuadrante

        # loop de cuadrante 3 x 3
        for x in range(row_start, row_start + 3):
            for y in range(col_start, col_start + 3):
                box.append(grid[x][y]) # apenda todos los numeros del cuadrante

        # si el numero no esta en su fila ni en su columna ni en su cuadrante: devuelve True
        if (number not in grid[row]) and (number not in column) and (number not in box):
            return True

    # metodo que devuelve una grilla valida
    def valid_grid(self):
        numbers = range(0,10) # lista de numeros
        row = 0 # inicia [row] en 0
        while row < 9: # recorre las filas
            resets = 0 # contador de resets por fila
            while 0 in self.grid[row]: # mientras haya un 0 en la fila hacer loop
                for col in range(9): # recorre las columnas
                    unused_numbers = list(set(numbers) ^ set([self.grid[x][col] for x in range(9)] + self.grid[row] + self.check_box(self.grid,row,col))) ###
                    # unused_numbers =  lista de numeros disponibles segun la posicion (segun columna, fila y cuadrante)
                    for _ in unused_numbers: # prueba con cada numero de la lista [unused_numbers]
                        number = random.choice(unused_numbers) # guarda un numero aleatorio de la lista de numeros sin usar
                        if self.check_number(self.grid,row,col,number): # si el check_number es verdadero
                            self.grid[row][col] = number # lo guarda en la posicion
                            break # rompe el loop para cambiar de columna
                    else: # si no se puede poner ningun numero de la lista de numeros sin usar
                        resets += 1 # aumenta el contador de resets de fila
                        if resets > 4: # si los resets son mayor a 4: reinicia la fila actual, vuelve a la fila anterior y la reinicia
                            self.grid[row] = [0 for x in range(9)] # reinicia la fila actual
                            row -= 1 #vuelve a la fila anterior
                            self.grid[row] = [0 for x in range(9)] # reinicia la fila actual
                            resets = 0 #reinicia los resets
                            break # rompe el loop de 0 en fila
                        else: # si los resets no son mayores a 4: reinicia la fila
                            self.grid[row] = [0 for x in range(9)] # reinicia la fila actual
                            break # rompe el loop de 0 en fila
            row += 1 # pasa a la siguiente fila
        return self.grid


sudoku = Sudoku_generator()
print_grid(sudoku.valid_grid())

# print(sudoku)

elapsed_time = datetime.now() - start_time 
print(f'\nElapsed time: {elapsed_time}\n')