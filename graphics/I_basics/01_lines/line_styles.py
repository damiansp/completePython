from tkinter import *

root = Tk()
root.title('Variations in line options')

WIDTH = 500
HEIGHT = 200

canvas = Canvas(root, width=WIDTH, height=HEIGHT, background='pink')
canvas.grid(row=0, column=1)

x1 = 10
y1 = HEIGHT / 2
x2 = WIDTH - 10
y2 = [40, 80, 120, 160]

canvas.create_line(x1, y1, x2, y2[0], dash=(3, 5), width=3)
canvas.create_line(x1, y1, x2, y2[1], dash=(9,), width=5, fill='red')
canvas.create_line(x1, y1, x2, y2[2], dash=(19,), width=10, fill='yellow')
canvas.create_line(x1, y1, x2, y2[3])

root.mainloop()
