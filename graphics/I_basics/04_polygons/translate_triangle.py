import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color, translate_shape

def main():
    root = Tk()
    root.title('Triangle')

    W, H = 700, 700
    PAD = 40
    N_TRIANGLE = 300
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    points = [get_random_point(W, H) for j in range(3)]
    
    for i in range(N_TRIANGLE):
        trans_x = random.choice(range(-10, 20, 2))
        trans_y = random.choice(range(-10, 20, 2))
        color1 = random_color()
        color2 = random_color()
        make_triangle(canvas, points, color1, color2)

        points = translate_shape(points, trans_x, trans_y)
                

    root.mainloop()


def make_triangle(canvas, points, color, outline):
    points = [point.as_list() for point in points]
    canvas.create_polygon(points, fill=color, outline=outline, width=3)


def get_random_point(max_w, max_h):
    return Point(int(random.uniform(0, max_w)), int(random.uniform(0, max_h)))


if __name__ == '__main__':
    main()
