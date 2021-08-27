import sys
from tkinter import *

sys.path.append('../../')
from util import make_regular_poly, Point, random_color

def main():
    root = Tk()
    root.title('Regular Polygons')

    W, H = 700, 500
    PAD = 20
    CENTER = Point(W / 2, H / 2)
    REVERSE = False
    radius = H / 2 - PAD
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    for i in range(12):
        sides = i + 3 if not REVERSE else 12 - i + 2
        poly = make_regular_poly(sides, CENTER, radius)
        poly_list = [point.as_list() for point in poly]
        canvas.create_polygon(
            poly_list, fill=random_color(), outline=random_color(), width=2)
        radius -= PAD
    
    root.mainloop()




if __name__ == '__main__':
    main()
