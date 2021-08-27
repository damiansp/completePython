#!/usr/bin/env python3

from tkinter import *

root = Tk()
canvas = Canvas(root, width=200, height=200)

canvas.grid(row=0, column=1)
canvas.create_line(10, 20, 50, 100)

root.mainloop()
