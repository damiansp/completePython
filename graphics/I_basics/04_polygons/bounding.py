import random
import sys
from tkinter import *

sys.path.append('../../')
from util import locate, Point, random_color

def main():
    root = Tk()
    root.title('Bounding Boxes')

    W, H = 700, 500
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    N_TRIANGLE = 10
    BOUND_COLOR = '#ff0000'

    triangles = [make_triangle(W, H) for i in range(N_TRIANGLE)]
    for triangle in triangles:
        bb = locate(triangle)['bb']
        bb = [point.as_list() for point in bb]
        triangle = [point.as_list() for point in triangle]
        canvas.create_polygon(triangle, fill=random_color())
        canvas.create_rectangle(bb, fill=None, outline=BOUND_COLOR)
    
    root.mainloop()


def make_triangle(max_width, max_height):
    points = [random_point(max_width, max_height) for point in range(3)]
    return points


def random_point(max_width, max_height):
    return Point(int(random.uniform(0, max_width)),
                 int(random.uniform(0, max_height)))
    



if __name__ == '__main__':
    main()
