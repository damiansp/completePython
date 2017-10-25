from tkinter import *

root = Tk()
root.title('Round line end-caps')

HEIGHT, WIDTH = 130, 450
PAD = 20
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(row=0, column=1)

x1 = PAD
y1 = PAD
x2 = WIDTH - PAD
y2 = PAD

for i in range(5):
    canvas.create_line(
        x1, y1 + 20*i, x2, y2 + 20*i, capstyle=ROUND, width=2**i)

canvas.mainloop()
