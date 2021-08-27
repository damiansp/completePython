from tkinter import *

root = Tk()
root.title('Cirle from Radius and Center')

W, H = 700, 700
PAD = 50
canvas = Canvas(root, width=W, height=H, background='black')

canvas.grid(row=0, column=1)

center = W / 2, H / 2
radius = W/2 - PAD
colors = ['red', 'blue']

def rc2bb(r, c):
    '''radius, center to bounding box'''
    return c[0] - r, c[1] - r, c[0] + r, c[1] + r

for i in range(6):
    canvas.create_oval(
        rc2bb(radius, center), fill=colors[i %2], width=5, outline='white')
    radius -= PAD
    
root.mainloop()

