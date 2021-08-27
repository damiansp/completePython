from tkinter import *

root = Tk()
root.title('Overlapping Rectangles')

WIDTH, HEIGHT = 700, 500
RECT_WIDTH, RECT_HEIGHT = 140, 100
DX, DY = 35, 25
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background='black')
colors = ['darkblue', 'turquoise', 'darkred']
#colors = ['gray', 'gray', 'gray']
stippling = ['gray25', 'gray50', 'gray75']

canvas.grid(row=0, column=1)

for i in range(12):
    canvas.create_rectangle((i + 1)*DX, (i +1)*DY,
                            (i + 1)*DX + RECT_WIDTH, (i + 1)*DY + RECT_HEIGHT,
                            fill=colors[i % 3],
                            stipple=stippling[i % 3],
                            outline=colors[(i + 1) % 3],
                            width=2*(i + 1),
                            dash=(26 - i))

root.mainloop()
