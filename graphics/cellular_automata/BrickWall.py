#!/usr/bin/env/ python3
# TODO: add color
# TODO: add user interface

from math import ceil
from tkinter import *

def main():
    root = Tk()
    W, H = 1400, 750
    BRICK_HEIGHT = 10
    PALLETTE = ['#000000', '#888888', '#FFFFFF']
    canvas = Canvas(root, width=W, height=H)

    root.title('Wall')
    canvas.grid(row=0, column=1)

    wall = BrickWall(canvas, BRICK_HEIGHT, initialize='random')
    wall.draw()

    root.mainloop()


class BrickWall:
    def __init__(self, canvas, row_height):
        self.canvas = canvas
        self.row_height = row_height
        self.n_row = int(ceil(canvas.winfo_reqheight() / row_height))

        
    def build(self):
        return [RowOfBricks(self.canvas, self.row_height, row)
                for row in range(self.n_row)]

    
    def draw(self):
        wall = self.build()
        [row.draw() for row in wall]
        

    
class RowOfBricks:
    def __init__(self, canvas, height, index):
        self.canvas = canvas
        self.height = height
        self.index = index
        self.width = canvas.winfo_reqwidth()
        self.y1 = height * index
        brick_width = 2 * self.height
        self.n_bricks = int(ceil(self.width / brick_width))

        
    def build(self):
        return [Brick(self.canvas, self.height, [self.index, brick], '#880000')
                for brick in range(self.n_bricks)]


    def draw(self):
        row = self.build()
        [brick.draw() for brick in row]
            

        
class Brick:
    def __init__(self, canvas, height, index, color=None):
        self.index = index
        self.canvas = canvas
        self.height = height
        self.width = 2 * height
        self.row_number, self.brick_number = index
        self.offset = -height if self.row_number % 2 == 1 else 0
        self.x1 = self.brick_number * self.width + self.offset
        self.y1 = self.row_number * height
        self.x2, self.y2 = self.x1 + self.width, self.y1 + height
        self.color = color

        
    def __str__(self):
        return ('Brick %s (%d x %d) of color %s'
                % (str(self.index), self.width, self.height, self.color))


    def draw(self):
        self.canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill=self.color)


        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
        

        
    
if __name__ == '__main__':
    main()
