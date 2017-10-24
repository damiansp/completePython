from tkinter import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def circle_cr2bb(c, r):
    return c + Point(-r, -r), c + Point(r, r)

    
root = Tk()
root.title('Color Brightness Wedge')

W, H = 400, 600
PAD = 50
canvas = Canvas(root, width=W, height=H, background='white')

canvas.grid(row=0, column=1)

wedge_tip = Point(W / 2, H - PAD)
wedge_width = W - 2*PAD
wedge_height = H - 2*PAD
wedge_corner1 = wedge_tip + Point(-wedge_width / 2, -wedge_height)
wedge_corner2 = wedge_tip + Point(wedge_width / 2, -wedge_height)
wedge_color = '#660000'
wedge = [wedge_tip.x, wedge_tip.y,
         wedge_corner1.x, wedge_corner1.y,
         wedge_corner2.x, wedge_corner2.y]
colors = [
    '#000000', '#c80000', '#a00000', '#ff0000', '#ff5050', '#ff8c8c', '#ffc8c8']
radii = [17, 35, 53, 70, 53, 35, 15]

canvas.create_polygon(wedge, fill=wedge_color)

dc = wedge_height / (len(colors) + 1)

for i in range(len(colors)):
    center = Point(wedge_tip.x, wedge_tip.y - (i + 1)*dc)
    bb = circle_cr2bb(center, radii[i])
    canvas.create_oval(bb[0].x, bb[0].y, bb[1].x, bb[1].y,
                       fill=colors[i],
                       outline=colors[i])



root.mainloop()



