from tkinter import *

root = Tk()
root.title('')

W, H = 500, 500
canvas = Canvas(root, width=W, height=H, background='white')

canvas.grid(row=0, column=1)

bounding_box = [20, 20, 480, 480]

canvas.create_oval(bounding_box)
root.mainloop()
