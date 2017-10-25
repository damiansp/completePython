from tkinter import *

root = Tk()
root.title('Arrows')

HEIGHT, WIDTH = 450, 200
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.grid(row=0, column=1)

x1 = [33, 66, 99, 132, 165, 198]
y1 = [75, 150, 225, 300, 375, 450]
x2 = [132, 165, 198, 33, 66, 99]
y2 = [375, 450, 75, 150, 225, 300]
arrows = ['first', 'last', 'both', 'both', 'both', 'both']

for i in range(6):
    canvas.create_line(
        x1[i], y1[i], x2[i], y2[i], arrow=arrows[i], width=2 ** i)

root.mainloop()
