from tkinter import *
from tkinter import ttk
from tktooltip import ToolTip
from tkinter import messagebox
import random
from Sudoku import *
import time

MARGIN = 20 # Pixels around the board
SIDE = 50  # Width of every board cell
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

# variables globales
a_row,a_col = -1,-1
last_pos = tuple()
last_pos_list = []
hints = 5
grid = []
solved_grid = []
original_grid = []


root = Tk()
root.title("Sudoku")
root.geometry('490x608')
root.resizable(False, False)
root.iconbitmap('./assets/sudoku.ico')
root.config(bg='white')

frame0 = Frame(root, width=WIDTH,bg='white')
frame0.grid(row=0,column=0,sticky=W+E+N+S)

frame1 = Frame(root,width=WIDTH, height=HEIGHT,bg='white')
frame1.grid(row=1,column=0)

frame2 = Frame(root,width=WIDTH,bg='white')
frame2.grid(row=2,column=0)

canvas = Canvas(frame1,width=WIDTH, height=HEIGHT,highlightthickness=0,bg='white')
canvas.pack(expand=YES, fill=BOTH)


# funcion para generar nueva partida
def new_game():
    global grid
    global hints
    global original_grid
    global solved_grid
    solved_grid = [[6, 5, 1, 7, 3, 9, 2, 4, 8], [3, 4, 2, 8, 6, 1, 7, 9, 5], [9, 7, 8, 4, 2, 5, 6, 1, 3], [7, 6, 4, 1, 5, 8, 9, 3, 2], [2, 8, 5, 3, 9, 7, 4, 6, 1], [1, 3, 9, 6, 4, 2, 8, 5, 7], [5, 9, 7, 2, 1, 4, 3, 8, 6], [4, 2, 6, 5, 8, 3, 1, 7, 9], [8, 1, 3, 9, 7, 6, 5, 2, 4]]
    grid = [[6, 5, 0, 7, 3, 9, 2, 0, 8], [3, 4, 2, 0, 6, 0, 7, 9, 5], [0, 7, 8, 4, 2, 0, 6, 0, 3], [0, 6, 4, 0, 5, 8, 9, 3, 0], [2, 8, 5, 0, 9, 7, 4, 6, 1], [1, 3, 9, 6, 4, 2, 8, 5, 0], [5, 9, 7, 2, 1, 0, 0, 0, 6], [4, 2, 6, 5, 0, 0, 1, 7, 9], [0, 0, 3, 0, 7, 6, 5, 2, 4]]
    canvas.delete('number')
    canvas.delete('cursor')
    canvas.delete('helps')
    hints = 5
    hints_label.config(text='Hints left: ' +str(hints))
    new_solved_grid = valid_grid()
    print(new_solved_grid)
    new_grid = delete_random(new_solved_grid,5)
    print(new_grid)
    # grid = new_grid
    # solved_grid = new_solved_grid
    original_grid = tuple(tuple(x) for x in grid)
#     print(original_grid)
    timer()
    fill_grid(grid)


# funcion para resetear la partida
def reset_grid():
    global grid
    global hints
    global original_grid
    if grid:
        canvas.delete('number')
        grid = list(list(x) for x in original_grid)
        canvas.delete('helps')
        hints = 5
        hint_button.config(state=NORMAL)
        hints_label.config(text='Hints left: ' +str(hints))
        fill_grid(grid)
        print(hints)

# funcion para deshacer
def step_back():
    global last_pos
    global last_pos_list
    global grid
    global hints
    canvas.delete('cursor')
    if len(last_pos_list) > 0:
        last_pos = last_pos_list[-1]
        grid[last_pos[0]][last_pos[1]] = 0
        last_pos_list.pop()
        canvas.delete('number')
        fill_grid(grid)
        print(hints)

# funcion para descubrir una pista al azar
def random_hint():
    global grid
    global last_pos_list
    global hints
    canvas.delete('number')
    canvas.delete('cursor')
    canvas.delete('helps')
    row = random.choice(range(9))
    col = random.choice(range(9))
    if grid:
        while grid[row][col] != 0 and hints > 0:
            row = random.choice(range(9))
            col = random.choice(range(9))
        if hints <= 5 and hints != 0:    
            grid[row][col] = solved_grid[row][col]
        if (row,col) not in last_pos_list and original_grid[row][col] == 0:
            last_pos_list.append((row,col))
            print(row,col)
        if hints > 0:
            hints -= 1
        elif hints < 1:
            hint_button.config(state=DISABLED)
            hints = 0
        print(hints)
        hints_label.config(text='Hints left: ' +str(hints))
        fill_grid(grid)
    # hints_label.after(1000, hints_label.destroy())


# funcion para mostrar tiempo jugado
def timer():
    now = time.strftime("%H:%M:%S")
    timer_label.config(text=now)
    timer_label.after(1000, timer)

# BTN: new random game button
new_game_icon = PhotoImage(file='./assets/new_game.png')
new_game_button = ttk.Button(frame2,command=new_game,image=new_game_icon)
new_game_button.pack(ipadx=5,ipady=5,expand=True,side='left')
ToolTip(new_game_button,msg='New Game')

# BTN: step back button
back_icon = PhotoImage(file='./assets/back.png')
back_button = ttk.Button(frame2,command=step_back,image=back_icon)
back_button.pack(ipadx=5,ipady=5,expand=True,side='left')
ToolTip(back_button,msg='Step Back')

# BTN: random hint
hint_icon = PhotoImage(file='./assets/hint.png')
hint_button = ttk.Button(frame2,command=random_hint,image=hint_icon)
hint_button.pack(ipadx=5,ipady=5,expand=True,side='left')
ToolTip(hint_button,msg='Random Hint')

# BTN: reset button
restart_icon = PhotoImage(file='./assets/restart.png')
restart_button = ttk.Button(frame2,command=reset_grid,image=restart_icon)
restart_button.pack(ipadx=5,ipady=5,expand=True,side='left')
ToolTip(restart_button,msg='Restart Game')
# BTN: exit button
exit_icon = PhotoImage(file='./assets/exit.png')
exit_button = ttk.Button(frame2,command=lambda: root.quit(),image=exit_icon)
exit_button.pack(ipadx=5,ipady=5,expand=True,side='left')
ToolTip(exit_button,msg='Exit App')

# LBL: hints label
hints_label = Label(frame0,font=('Kanit SemiBold',14),fg='sea green',bg='white')
hints_label.grid(row=0,column=1,columnspan=1,ipadx=45)

# LBL: timer label
timer_label = Label(frame0,font=('Kanit SemiBold',14),fg='sea green',bg='white')
timer_label.grid(row=0,column=0,columnspan=1,ipadx=95)


# funcion para dibujar las cuadricula
def draw_grid():
    for _ in range(10):
        color = "gray45" if _ % 3 == 0 else "gray45"
        line_width = 3 if _ % 3 == 0 else 1

        x0 = MARGIN
        y0 = MARGIN + _ * SIDE
        x1 = HEIGHT - MARGIN
        y1 = MARGIN + _ * SIDE
        canvas.create_line(x0,y0,x1,y1,fill=color,width=line_width)

        x0 = MARGIN + _ * SIDE
        y0 = MARGIN
        x1 = MARGIN + _ * SIDE
        y1 = WIDTH - MARGIN
        canvas.create_line(x0,y0,x1,y1,fill=color,width=line_width)

# funcion para llenar la cuadricula con los numeros de grid
def fill_grid(grid):
    for row in range(9):
        for col in range(9):
            x = MARGIN + col * SIDE + SIDE / 2
            y = MARGIN + row * SIDE + SIDE / 2
            if grid[row][col] != 0:
                number = grid[row][col]
                color = "gray25" if grid[row][col] == original_grid[row][col] else "sea green" # si el numero mostrado esta o no esta en la grid original
                canvas.create_text(x,y,text=number,fill=color,font=("Kanit SemiBold", 18),tags='number')
            else:
                canvas.create_text(x,y)

    if grid != solved_grid:
        pass
    else:
        messagebox.showinfo(message="You WIN", title="Game over")
        print('WIN')

# funcion para hacer click izquierdo en la celda
def clicked_cell(event):
    global a_row
    global a_col
    x,y = event.x,event.y
    # print(x,y) # coordenadas
    if grid:
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            canvas.focus_set()
            
            # toma la posicion segun las coordenadas 
            row, col = int((y - MARGIN) / SIDE), int((x - MARGIN) / SIDE)
            print(f'numero: {grid[row][col]}, row: {row}, col: {col}')
            # si la posicion ya está seleccionada, la deselecciona
            if (row,col) == (a_row,a_col):
                a_row,a_col = -1,-1
            elif original_grid[row][col] == 0:
                a_row,a_col = row,col
            # print(a_row,a_col) # posicion
        else:
            a_row,a_col = -1,-1

        if event.num == 3:
            canvas.delete('helps')
            if grid[a_row][a_col] == 0:
                cell_notes()
        elif event.num == 1:
            selected_cell() # 
        # helps_cell()
        print(event.num)

# funcion para hacer un recuadro en la posicion seleccionada con click izquierdo
def selected_cell():
    global a_row
    global a_col
    canvas.delete('cursor')
    if a_row >= 0 and a_col >= 0 and original_grid[a_row][a_col] == 0:
        x0 = MARGIN + a_col * SIDE + 1
        y0 = MARGIN + a_row * SIDE + 1
        x1 = MARGIN + (a_col + 1) * SIDE - 1
        y1 = MARGIN + (a_row + 1) * SIDE - 1
        canvas.create_rectangle(x0,y0,x1,y1,outline='sea green',tags='cursor',width=3)

# funcion para mostrar anotaciones
def cell_notes():
    global a_row
    global a_col
    # canvas.delete('cursor')
    canvas.delete('helps')
    if a_row >= 0 and a_col >= 0 and original_grid[a_row][a_col] == 0:
        x0 = MARGIN + a_col * SIDE + 1
        y0 = MARGIN + a_row * SIDE + 1 
        canvas.create_text(x0+8,y0+8,text=1,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+24,y0+8,text=2,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+40,y0+8,text=3,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+8,y0+24,text=4,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+24,y0+24,text=5,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+40,y0+24,text=6,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+8,y0+40,text=7,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+24,y0+40,text=8,fill='gray',font=("Kanit SemiBold", 8),tags='helps')
        canvas.create_text(x0+40,y0+40,text=9,fill='gray',font=("Kanit SemiBold", 8),tags='helps') 

# funcion para hacerl recuadro en la posicion seleccionada con click derecho
def helps_cell():
    global a_row
    global a_col
    canvas.delete('cursor')
    canvas.delete('helps')
    if a_row >= 0 and a_col >= 0 and original_grid[a_row][a_col] == 0:
        x0 = MARGIN + a_col * SIDE + 1
        y0 = MARGIN + a_row * SIDE + 1
        x1 = MARGIN + (a_col + 1) * SIDE - 1
        y1 = MARGIN + (a_row + 1) * SIDE - 1
        canvas.create_rectangle(x0,y0,x1,y1,outline='gray',tags='cursor',width=3)


# funcion que ingresa valor por teclado
def key_pressed(event):
    global a_row
    global a_col
    global last_pos_list
    global hints
    if a_row >= 0 and a_col >= 0 and event.char in '1234567890':
        canvas.delete('number') # borra el numero de la posicion antes de agregar
        grid[a_row][a_col] = int(event.char)
        if (a_row, a_col) not in last_pos_list:
            canvas.delete('helps')
            last_pos_list.append((a_row, a_col))
        # selected_cell()
        fill_grid(grid)
        a_row,a_col = -1,-1
        print(hints)


canvas.bind('<Button-1>',clicked_cell) # bindeo al hacer click izquierdo en una celda
canvas.bind('<Button-3>',clicked_cell) # bindeo al hacer click izquierdo en una celda
canvas.bind('<Key>',key_pressed) # bindeo al ingresar un numero por teclado
draw_grid() # dibuja la cuadricula

# fill_grid(grid) # rellena la cuadricula


root.mainloop()
