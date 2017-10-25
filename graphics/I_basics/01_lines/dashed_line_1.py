from tkinter import *

WIDTH = 500
HEIGHT = 200

root = Tk()
root.title('Dashed Lines')

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(row=0, column=1)

x1 = [10, 20]
x2 = [400, 20]
dash = [12, 1]
line_width = 2

for i in range(3):
    canvas.create_line(x1[0], x1[1], x2[0], x2[1], dash=dash, width=line_width)
    x2[1] += 40
    dash[0] //= 2
    dash[1] *= 2
    line_width += 1

root.mainloop()


