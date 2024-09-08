import random

import numpy as np


DIM = 4
WIN = 2048


def start_game():
    mat = np.zeros((DIM, DIM), dtype=int)
    print_controls()
    mat = add_new_2(mat)
    return mat


def print_controls():
    print(
        "Commands are as follows:\n"
        "'W' or 'w' : Move Up\n"
        "'S' or 's' : Move Down\n"
        "'A' or 'a' : Move Left\n"
        "'D' or 'd' : Move Right\n")


def add_new_2(mat):
    'Add a new 2 at random in any empty grid cell'
    r = random.randint(0, DIM - 1)
    c = random.randint(0, DIM - 1)
    while mat[r, c] != 0:
        r = random.randint(0, DIM - 1)
        c = random.randint(0, DIM - 1)
    mat[r, c] = 2
    return mat


def get_current_state(mat):
    # if <WIN> in grid, you win
    for i in range(DIM):
        for j in range(DIM):
            if mat[i, j] == WIN:
                return 'WON'
    # if at least 1 empty cell, continue
    for i in range(DIM):
        for j in range(DIM):
            if not mat[i, j]:
                return 'CONTINUE'
    # if no empty cell, but legal move exists
    for i in range(DIM - 1):
        for j in range(DIM - 1):
            if mat[i, j] == mat[i + 1, j] or mat[i, j] == mat[i. j + 1]:
                return 'CONTINUE'
    for j in range(DIM - 1):
        if mat[DIM - 1, j] == mat[DIM - 1, j + 1]:
            return 'CONTINUE'
    for i in range(DIM - 1):
        if mat[i, DIM - 1] == mat[i + 1, DIM - 1]:
            return 'CONTINUE'
    return 'LOST'
            

def compress(mat):
    'Compress grid before AND after each cell merging'
    is_changed = False
    new_mat = np.zeros((DIM, DIM), dtype=int)
    for i in range(DIM):
        pos = 0
        for j in range(DIM):
            if mat[i, j]:
                new_mat[i, pos] = mat[i, j]
                if j != pos:
                    is_changed = True
                pos += 1
    return new_mat, is_changed


def merge(mat):
    'Merge cells in the matrix after compressing'
    is_changed = False
    for i in range(DIM):
        for j in range(DIM - 1):
            # if cell has same value as next, and is non-empty
            if mat[i, j] and mat[i, j] == mat[i, j + 1]:
                mat[i, j] *= 2
                mat[i, j + 1] = 0
                is_changed = True
    return mat, is_changed


def reverse(mat):
    'Reverses the content of each row'
    new_mat = np.array([row[::-1] for row in mat], dtype=int)
    return new_mat


def move_left(mat):
    mat, is_changed1 = compress(mat)
    mat, is_changed2 = merge(mat)
    is_changed = is_changed1 or is_changed2
    mat, _ = compress(mat)
    return mat, is_changed


def move_right(mat):
    'Reverse, move left, reverse back'
    mat = reverse(mat)
    mat, is_changed = move_left(mat)
    mat = reverse(mat)
    return mat, is_changed


def move_up(mat):
    mat = mat.T
    mat, is_changed = move_left(mat)
    mat = mat.T
    return mat, is_changed


def move_down(mat):
    mat = mat.T
    mat, is_changed = move_right(mat)
    mat = mat.T
    return mat, is_changed
