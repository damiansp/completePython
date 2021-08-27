import math
import sys
from copy import *
from tkinter import *

sys.path.append('../../')
from util import Point, rotate_shape

COLORS_1 = ['#550000', '#aa0000', '#ff0000', '#ffff00', '#00ff00', '#00ffff',
            '#0000ff', '#ff00ff', '#660066', '#330044']
COLORS_2 = ['#440000', '#ff0000', '#000000', '#ffff00', '#000000', '#00ff00',
            '#000000', '#00ffff', '#000000', '#0000ff', '#000000', '#ff00ff',
            '#440044']
line_1 = [
    Point(x, 420) for x in [20, 25, 32, 40, 50, 60, 70, 80, 88, 94, 100, 104]]
line_2 = [Point(x, 420) for x in range(160, 240, 5)]

def main():
    root = Tk()
    root.title('Double Rainbow All The Way!')

    W, H = 800, 450
    PAD = 20
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    center = Point(W / 2, H - PAD)

    make_rainbow(canvas, 10, line_1, COLORS_1, 720, 0.25, center, 3)
    make_rainbow(canvas, 12, line_2, COLORS_2, 360, 0.5, center, 2)

    root.mainloop()


def make_rainbow(
    canvas, n_color, line, colors, n_steps, degree_factor, center, width):
    
    for i in range(n_color):
        line_a = [Point(line[i].x, line[i].y),
                  Point(line[i+1].x, line[i+1].y)]
        for j in range(n_steps):
            new_shape = rotate_shape(line_a, center, degree_factor*j)
            new_shape = [point.as_list() for point in new_shape]
            canvas.create_line(new_shape, fill=colors[i], width=width)


if __name__ == '__main__':
    main()
