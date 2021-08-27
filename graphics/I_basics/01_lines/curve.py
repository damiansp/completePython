from tkinter import *

root = Tk()
root.title('Basic Curve')

OFFSET = 50
WIDTH, HEIGHT = 1000, 700
PAD = 20
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background='black')
canvas.grid(row=0, column=1)

x = [PAD, PAD, WIDTH - PAD - 10*OFFSET, WIDTH - PAD - 10*OFFSET]
y = [PAD, HEIGHT - PAD, HEIGHT - PAD, HEIGHT / 2]
canvas.create_line(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], fill='grey')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown',
          'grey', 'white', 'pink']
for i in range(10):
    canvas.create_line(x[0] + i*OFFSET, y[0],
                       x[1] + i*OFFSET, y[1],
                       x[2] + i*OFFSET, y[2],
                       x[3] + i*OFFSET, y[3],
                       fill=colors[i],
                       smooth='true',
                       splinesteps=i + 3)
root.mainloop()
