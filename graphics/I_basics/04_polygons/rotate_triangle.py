import random
import sys
from tkinter import *

sys.path.append('../../')
from util import locate, Point, rotate_shape, random_color

def main():
    root = Tk()
    root.title('Rescaling')

    W, H = 700, 500
    PAD = 50
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    #triangle = make_random_triangle(W, H)
    triangle = [
        Point(W / 2, PAD), Point(PAD, H - PAD), Point(W - 3*PAD, H - 4*PAD)]
    scale_factor = 0.8

    for i in range(37):
        color1 = random_color()
        color2 = random_color()
        center = locate(triangle)['center']
        t_list = [point.as_list() for point in triangle]
        print(t_list)
        canvas.create_polygon(
            t_list, fill=color1, outline=color2, width=2)
        triangle = rotate_shape(triangle, center, degrees=10)
        [print(point) for point in triangle]
        
    root.mainloop()




if __name__ == '__main__':
    main()
