# from tkinter import *
# from tkinter import ttk

# def savePosn(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y

# def addLine(event):
#     canvas.create_line((lastx, lasty, event.x, event.y))
#     savePosn(event)

# root = Tk()
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# canvas = Canvas(root)
# canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# canvas.bind("<Button-1>", savePosn)
# canvas.bind("<B1-Motion>", addLine)

# root.mainloop()

# from tkinter import *

# def say_hi():
#     print("hello ~ !")

# root = Tk()

# frame1 = Frame(root)
# frame2 = Frame(root)
# root.title("tkinter frame")

# label= Label(frame1,text="Label",justify=LEFT)
# label.pack(side=LEFT)

# hi_there = Button(frame2,text="say hi~",command=say_hi)
# hi_there.pack()

# frame1.pack(padx=1,pady=1)
# frame2.pack(padx=10,pady=10)

# root.mainloop()

# import tkinter as tk 
 
# class App(tk.Tk): 
#     def __init__(self): 
#         super().__init__() 
#         entry = tk.Entry(self) 
#         entry.bind("<FocusIn>", self.print_type)  
#         entry.bind("<Key>", self.print_key) 
#         entry.pack(padx=20, pady=20) 
 
#     def print_type(self, event): 
#         print(event.type) 
 
#     def print_key(self, event): 
#         args = event.keysym, event.keycode, event.char 
#         print("Symbol: {}, Code: {}, Char: {}".format(*args))
#         print(type(event.keysym),type(event.char))
 
# if __name__ == "__main__": 
#     app = App() 
#     app.mainloop() 

#import the tkinter library

# from tkinter import *

# #define the messagebox function
# def messagebox():

# #toplevel function creates MessageBox dialog which appears on top of the screen
#    top=Toplevel(win)
#    top.title("Click Me")
#    #Define the position of the MessageBox
#    x_position = 600
#    y_position = 400
#    top.geometry(f"600x200+{x_position}+{y_position}")
#    #Define the property of the messageBox
#    l1=Label(top, text= "Hello! TutorialsPoint",bg= "green", fg=
# "white",font=('Times New Roman', 24),height=50, width= 50).pack()

# #Create an instance of the tkinter frame
# #And resize the frame
# win = Tk()
# win.geometry("600x200")
# win.title("Window-1")
# Button(win, text="Click Me", command=messagebox,
# width=8).pack(pady=80)

# win.mainloop()

# from tkinter import ttk
# import tkinter as tk
# from tkinter.messagebox import showinfo


# # root window
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')


# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"


# def progress():
#     if pb['value'] < 100:
#         pb['value'] += 20
#         value_label['text'] = update_progress_label()
#     else:
#         showinfo(message='The progress completed!')


# def stop():
#     pb.stop()
#     value_label['text'] = update_progress_label()


# # progressbar
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='determinate',
#     length=280
# )
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# # label
# value_label = ttk.Label(root, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)

# # start button
# start_button = ttk.Button(
#     root,
#     text='Progress',
#     command=progress
# )
# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=stop
# )
# stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


# root.mainloop()

