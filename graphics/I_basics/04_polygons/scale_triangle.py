import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, rescale, random_color

def main():
    root = Tk()
    root.title('')

    W, H = 700, 500
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    #triangle = make_random_triangle(W, H)
    triangle = [Point(10, 10), Point(10, 50), Point(50, 10)]
    scale_factor = 1.5

    for i in range(10):
        color1 = random_color()
        color2 = random_color()
        t_list = [point.as_list() for point in triangle]
        print(t_list)
        canvas.create_polygon(
            t_list, fill=color1, outline=color2, width=(i + 1)*scale_factor)
        triangle = rescale(triangle, scale_factor)
        [print(point) for point in triangle]
        
    root.mainloop()


def make_random_triangle(max_width, max_height):
    return [Point(int(random.uniform(0, max_width)),
                  int(random.uniform(0, max_height)))
            for i in range(3)]



if __name__ == '__main__':
    main()
