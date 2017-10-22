from tkinter import *

root = Tk()
root.title('Cirle from Radius and Center')

W, H = 700, 700
PAD = 5
canvas = Canvas(root, width=W, height=H, background='black')

canvas.grid(row=0, column=1)

center = W / 2, H / 2
radius1 = W/2 - PAD
radius2 = 5 * PAD
colors = ['#FF8844', '#ff8800', '#ff875c', '#ff8717', '#ff86d4', '#ff8690',
          '#ff864c', '#ff8608', '#ff85c4', '#ff8580', '#ff853c']

    

def rcs2bb(r1, r2, c):
    '''radius, center to bounding box'''
    return c[0] - r1, c[1] - r2, c[0] + r1, c[1] + r2

for i in range(60):
    canvas.create_oval(rcs2bb(radius1, radius2, center),
                       width=2,
                       outline=colors[i % 11])
    radius1 -= PAD
    radius2 += PAD
    
root.mainloop()

