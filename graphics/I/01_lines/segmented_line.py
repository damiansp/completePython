from tkinter import *

root = Tk()
HEIGHT, WIDTH = 300, 300
PAD = 20
canvas = Canvas(root, height=HEIGHT, width=WIDTH, background='black')

canvas.grid(row=0, column=1)

points = [(PAD, PAD), (PAD, HEIGHT - PAD), (WIDTH - PAD, HEIGHT - PAD)]

canvas.create_line(points[0][0], points[0][1],
                   points[1][0], points[1][1],
                   points[2][0], points[2][1],
                   fill='pink',
                   width=4,
                   capstyle=ROUND)
canvas.mainloop()
