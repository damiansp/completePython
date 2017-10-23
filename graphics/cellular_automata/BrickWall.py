#!/usr/bin/env python3
# TODO: add user interface

import numpy as np
from math import ceil
from tkinter import *


def main():
    root = Tk()
    W, H = 1400, 750
    BRICK_HEIGHT = 5
    canvas = Canvas(root, width=W, height=H)

    root.title('Wall')
    canvas.grid(row=0, column=1)

    wall = BrickWall(canvas, BRICK_HEIGHT)
    wall.draw()

    root.mainloop()


class BrickWall:
    def __init__(self, canvas, row_height):
        self.canvas = canvas
        self.row_height = row_height
        self.n_row = int(ceil(canvas.winfo_reqheight() / row_height))

        
    def build(self):
        wall = [RowOfBricks(self.canvas, self.row_height, 0)]
        for row in range(1, self.n_row):
            wall.append(RowOfBricks(
                self.canvas, self.row_height, row, previous_row=wall[row -1]))
        return wall

    
    def draw(self):
        wall = self.build()
        [row.draw() for row in wall]
        

    
class RowOfBricks:
    def __init__(self, canvas, height, index, previous_row=None,
                 new_color_method='random'):
        self.canvas = canvas
        self.height = height
        self.index = index
        self.previous_row = previous_row
        self.previous_row = previous_row
        self.new_color_method = new_color_method
        self.width = canvas.winfo_reqwidth()
        self.y1 = height * index
        brick_width = 2 * self.height
        self.n_bricks = int(ceil(self.width / brick_width))
        self.brick_list = self.build()

        
    def build(self):
        if not self.previous_row:
            return [Brick(self.canvas,
                          self.height,
                          [self.index, brick],
                          self.get_new_color(self.new_color_method))
                    for brick in range(self.n_bricks)]
        else:
            return [Brick(self.canvas,
                          self.height,
                          [self.index, brick],
                          self.determine_color(self.index, brick))
                    for brick in range(self.n_bricks)]


    def get_new_color(self, method):
        if self.new_color_method == 'random':
            return np.random.choice(PALETTE);
        else:
            print('new_color_method() not defined, using "random"')
            get_new_color(self, 'random')


    def determine_color(self, row_index, brick_index):
        offset = True if row_index % 2 == 1 else False
        if not offset:
            parent_colors = (self.previous_row.brick_list[brick_index].color,)
            try:
                parent_colors += (
                    self.previous_row.brick_list[brick_index + 1].color,)
            except IndexError:
                parent_colors += (self.get_new_color(self.new_color_method),)
        else:
            try:
                parent_colors = (
                    self.previous_row.brick_list[brick_index - 1].color,)
            except IndexError:
                parent_colors = (self.get_new_color(self.new_color_method))
            parent_colors += (self.previous_row.brick_list[brick_index].color,)

        return COLOR_ASSIGNMENT_RULES[parent_colors]

    
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
        self.canvas.create_rectangle(self.x1,
                                     self.y1,
                                     self.x2,
                                     self.y2,
                                     fill=self.color,
                                     outline=self.color)


        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
        

        
    
if __name__ == '__main__':
    def random_color():
        digits = list('0123456789abcdef')
        return '#' + ''.join([np.random.choice(digits) for i in range(6)])
    
    PALETTE = tuple([random_color() for i in range(3)])
    #keys = ((a, b) for a in PALETTE for b in PALETTE)
    #COLOR_ASSIGNMENT_RULES = dict.fromkeys(keys, 0)
    COLOR_ASSIGNMENT_RULES = {(PALETTE[0], PALETTE[0]): PALETTE[0],
                              (PALETTE[0], PALETTE[1]): PALETTE[0],
                              (PALETTE[0], PALETTE[2]): PALETTE[1],
                              (PALETTE[1], PALETTE[0]): PALETTE[1],
                              (PALETTE[1], PALETTE[1]): PALETTE[2],
                              (PALETTE[1], PALETTE[2]): PALETTE[2],
                              (PALETTE[2], PALETTE[0]): PALETTE[2],
                              (PALETTE[2], PALETTE[1]): PALETTE[1],
                              (PALETTE[2], PALETTE[2]): PALETTE[0]}

    main()
