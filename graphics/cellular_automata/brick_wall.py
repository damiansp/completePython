from math import ceil
from tkinter import *

W, H = 1400, 750
BRICK_H = 10
BRICK_W = 2 * BRICK_H


def main():
    root = Tk()
    canvas = Canvas(root, width=W, height=H, background='white')

    root.title('Brick Wall')
    canvas.grid(row=0, column=1)
    build_wall(canvas)
    root.mainloop()

    
def build_wall(canvas):
    n_row = int(ceil(H / BRICK_H))

    for row in range(n_row):
        add_row_of_bricks(canvas, row)
                
    
def add_row_of_bricks(canvas, row):
    offset = -BRICK_W / 2 if row % 2 == 1 else 0
    n_bricks = int(ceil(W / BRICK_W))

    for brick in range(n_bricks):
        add_brick(canvas, row, brick, offset)


def add_brick(canvas, row, brick_number, offset):
    x1 = brick_number * BRICK_W + offset
    x2 = x1 + BRICK_W
    y1 = row * BRICK_H
    y2 = y1 + BRICK_H
    canvas.create_rectangle(x1, y1, x2, y2)
                   

if __name__ == '__main__':
    main()






