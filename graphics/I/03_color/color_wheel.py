import math
from tkinter import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def circle_cr2bb(c, r):
    return c - Point(r, r), c + Point(r, r)


def rotate(center, point, angle):
    rad = math.radians(angle)
    a_rad = math.atan2((point.y - center.y), (point.x - center.x))
    a_len = center.distance_to(point)
    rad += a_rad
    #deg = math.degrees(rad)
    new_x = a_len * math.cos(rad)
    new_y = a_len * math.sin(rad)
    return Point(new_x, new_y)#, deg


def segment_background(color, angle, p1, p2, origin, canvas):
    def update_point(p):
        new_p = rotate(origin, p, angle)
        return new_p + origin
    
    p1 = update_point(p1)
    p2 = update_point(p2)
    wedge = [origin.x, origin.y, p1.x, p1.y, p2.x, p2.y]
    canvas.create_polygon(wedge, fill=color)

    
root = Tk()
root.title('Color Brightness Wedge')

W, H = 600, 600
PAD = 20
canvas = Canvas(root, width=W, height=H, background='white')
canvas.grid(row=0, column=1)

theta_deg = 0.
origin = Point(W / 2, H / 2)
wedge_width = W / 5
wedge_height = (H / 2) - PAD
p2 = origin + Point(-wedge_width / 2, -wedge_height)
p3 = origin + Point(wedge_width / 2, -wedge_height)
wedge = [origin, p2, p3]

diameter = wedge_width
height = wedge_height / 2

reds = ['#380000', '#6e0000', '#a00000', '#ff0000',
        '#ff5050', '#ff8c8c', '#ffc8c8', '#440000']
khakis = ['#303000', '#606000', '#8f9f00', '#b3b300',
          '#d6d600', '#dbdb30', '#dbdb77', '#3e2700']
yellows = ['#383800', '#6e6e00', '#a0a000', '#ffff00',
           '#ffff50', '#ffff8c', '#ffffc8', '#444400']
oranges = []
greens  = []
dk_greens = []
cyans     = []
steelblues = []
blues      = []
purples    = []
crimsons   = []
magentas   = []

angles = range(0, 360, 30)
colors = [reds, khakis, yellows, oranges, greens, dk_greens, cyans, steelblues,
          blues, purples, crimsons, magentas]

for i in range(len(colors)):
    segment_background(reds[0], angles[i], p2, p3, origin, canvas)
root.mainloop()



