from tkinter import *

root = Tk().title('Rectangle')

HEIGHT, WIDTH = 500, 700
PAD = 20
canvas = Canvas(root, height=HEIGHT, width=WIDTH, background='black')
colors = ['darkblue', 'darkred', 'darkgreen', 'black']
canvas.grid(row=0, column=1)

for i in range(4):
    pad = PAD * (i + 1)
    canvas.create_rectangle(pad, pad, WIDTH - pad, HEIGHT - pad, fill=colors[i])

canvas.mainloop()
