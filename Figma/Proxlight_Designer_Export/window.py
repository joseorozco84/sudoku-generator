from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("500x650")
window.configure(bg = "#c29c39")
canvas = Canvas(
    window,
    bg = "#c29c39",
    height = 650,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    374.5, 44.0,
    text = "Hints left: 5",
    fill = "#000000",
    font = ("None", int(20.0)))

canvas.create_text(
    95.5, 44.0,
    text = "00:01",
    fill = "#000000",
    font = ("None", int(20.0)))

img0 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 138, y = 574,
    width = 78,
    height = 55)

img1 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 289, y = 574,
    width = 78,
    height = 55)

img2 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 211, y = 574,
    width = 78,
    height = 55)

img3 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 368, y = 574,
    width = 78,
    height = 55)

img4 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 51, y = 574,
    width = 78,
    height = 55)

img5 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 26, y = 29,
    width = 30,
    height = 30)

img6 = PhotoImage(file = f"./figma/Proxlight_Designer_Export/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 444, y = 29,
    width = 30,
    height = 30)

window.resizable(False, False)
window.mainloop()
