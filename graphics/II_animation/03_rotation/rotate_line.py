import random
import sys
from tkinter import *

sys.path.append('../../')
from util import (make_discrete_color_series, Point, random_color, rotate)

W, H = 600, 750
CENTER = Point(W/2, H/2)
CYCLE_IN_MS = 50
DEG_INCR1 = random.uniform(-1, 1)
DEG_INCR2 = random.uniform(-2, 2)
N_STEPS = 1000
N_LINES = 3


def main():
    root = Tk()
    root.title('Rotating line')

    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    lines = [random_line() for line in range(N_LINES)]
    colors = [
        make_discrete_color_series(random_color(), random_color(), N_STEPS)
        for color in range(N_LINES)]
    centers = [random_point() for line in range(N_LINES)]

    for i in range(N_STEPS):
        for j in range(len(lines)):
            lines[j] = rotate(lines[j], DEG_INCR1, centers[j])
            lines[j] = rotate(lines[j],
                              (j+2) * DEG_INCR2,
                              (lines[j][0] + lines[j][1]) * 0.5)
            canvas.create_line(
                lines[j][0].as_list(), lines[j][1].as_list(), fill=colors[j][i])
        canvas.update()
        canvas.after(CYCLE_IN_MS)
    
    root.mainloop()


def random_line():
    return [random_point() for point in range(2)]


def random_point():
    return Point(random.uniform(0, W), random.uniform(0, H))


if __name__ == '__main__':
    main()
