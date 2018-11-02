#!/usr/bin/env python3
# TODO: make options as command line tool

import numpy as np
from math import ceil
from pprint import pprint
from tkinter import *


def main():
    root = Tk()
    CANVAS_WIDTH, CANVAS_HEIGHT = 700, 750
    BRICK_HEIGHT = 2
    
    # How to assign colors for initial or off-screen bricks:
    # Choices:
    #   random: 
    #   constant: [0, 0, 0, 0, ...],
    #   alt2, [0, 1, 0, 1, 0, 1, ...]
    #   alt3, [0, 1, 2, 0, 1, 2, 0, 1, 2, ...]
    #   or (TODO) a list indicating the sequence
    #   e.g. [0, 1, 2, 0, 0, 1, 1, 2, 2] where 0, 1, 2 are the colors in PALETTE
    NEW_COLOR_OPTIONS = ['random', 'constant', 'alt2', 'alt3']

    # Initial row
    INIT = np.random.choice(NEW_COLOR_OPTIONS)

    # New off-screen bricks
    OFF_SCREEN = np.random.choice(NEW_COLOR_OPTIONS)\
                 if INIT == 'random' else 'random' # prevent many trivial cases
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    root.title('Init: %s; New: %s' % (INIT, OFF_SCREEN))
    canvas.grid(row=0, column=1)
    wall = BrickWall(canvas, BRICK_HEIGHT, init=INIT, off_screen=OFF_SCREEN)
    wall.draw()
    root.mainloop()


class BrickWall:
    def __init__(self, canvas, row_height, init, off_screen):
        self.canvas = canvas
        self.row_height = row_height
        self.init = init
        self.off_screen = off_screen
        self.n_row = int(ceil(canvas.winfo_reqheight() / row_height))

    def build(self):
        wall = [
            RowOfBricks(
                self.canvas, self.row_height, 0, init_color_method=self.init)]
        for row in range(1, self.n_row):
            wall.append(RowOfBricks(self.canvas,
                                    self.row_height,
                                    row,
                                    previous_row=wall[row -1],
                                    new_color_method=self.off_screen))
        return wall
    
    def draw(self):
        wall = self.build()
        [row.draw() for row in wall]
        

    
class RowOfBricks:
    def __init__(
            self, canvas, height, index, previous_row=None,
            init_color_method='random', new_color_method='random'):
        self.canvas = canvas
        self.height = height
        self.index = index
        self.previous_row = previous_row
        self.previous_row = previous_row
        self.init_color_iterator = ColorIterator(init_color_method)
        self.new_color_iterator = ColorIterator(new_color_method)
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
                          next(self.init_color_iterator))
                    for brick in range(self.n_bricks)]
        else:
            return [Brick(self.canvas,
                          self.height,
                          [self.index, brick],
                          self.determine_color(self.index, brick))
                    for brick in range(self.n_bricks)]

    def determine_color(self, row_index, brick_index):
        error = np.random.choice([True, False],
                                 p=[ERROR_PROBABILITY, 1 - ERROR_PROBABILITY])
        if error:
            return np.random.choice(PALETTE)        
        offset = True if row_index % 2 == 1 else False
        if offset:
            # Deterministic rules...
            #brick_index -= 1
            # ...or slight randomness
            brick_index -= np.random.choice([-1, 0, 1], p=[0.09, 0.9, 0.01])
        parent_colors = []
        for i in range(2):
            try:
                parent_colors.append(
                    self.previous_row.brick_list[brick_index + i].color)
            except IndexError:
                parent_colors.append(next(self.new_color_iterator))
        return COLOR_ASSIGNMENT_RULES[tuple(parent_colors)]
    
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


class ColorIterator:
    def __init__(self, method='random'):
        self.method = method
        self.color1, self.color2, self.color3 = PALETTE

    def __next__(self):
        if self.method == 'random':
            return np.random.choice(PALETTE)
        elif self.method == 'constant':
            return self.color1
        elif self.method == 'alt2':
            self.color1, self.color2 = self.color2, self.color1
            return self.color1
        elif self.method == 'alt3':
            self.color1, self.color2, self.color3 = (
                self.color2, self.color3, self.color1)
            return self.color1
    
    def __iter__(self):
        return self

    
def random_color():
    digits = list('0123456789abcdef')
    return '#' + ''.join([np.random.choice(digits) for i in range(6)])
    

        
    
if __name__ == '__main__':
    PALETTE = tuple([random_color() for i in range(3)])
    ERROR_PROBABILITY = 0
    
    # Random rule assigment...
    keys = ((a, b) for a in PALETTE for b in PALETTE)
    COLOR_ASSIGNMENT_RULES = dict.fromkeys(keys, 0)
    for key in COLOR_ASSIGNMENT_RULES:
        COLOR_ASSIGNMENT_RULES[key] = np.random.choice(PALETTE)    
    pprint(COLOR_ASSIGNMENT_RULES)
        
    # ...or hard code rules:
    '''
    COLOR_ASSIGNMENT_RULES = {(PALETTE[0], PALETTE[0]): PALETTE[0],
                              (PALETTE[0], PALETTE[1]): PALETTE[0],
                              (PALETTE[0], PALETTE[2]): PALETTE[1],
                              (PALETTE[1], PALETTE[0]): PALETTE[1],
                              (PALETTE[1], PALETTE[1]): PALETTE[2],
                              (PALETTE[1], PALETTE[2]): PALETTE[2],
                              (PALETTE[2], PALETTE[0]): PALETTE[2],
                              (PALETTE[2], PALETTE[1]): PALETTE[1],
                              (PALETTE[2], PALETTE[2]): PALETTE[0]}
        '''
    main()
