# TODO:
# - refactor
# - use numpy implementation of <mat>
import random


DIM = 4
WIN = 2048


def start_game():
    mat = []
    for in range(DIM):
        mat.append([0] * DIM)
    print_controls()
    add_new_2(mat)
    return mat


def print_controls():
    print(
        "Commands are as follows :\n"
        "'W' or 'w' : Move Up\n"
        "'S' or 's' : Move Down\n"
        "'A' or 'a' : Move Left\n"
        "'D' or 'd' : Move Right\n")


def add_new_2(mat):
    'Add a new 2 at random in any empty grid cell'
    # code appears to be faulty
    r = random.randint(0, DIM - 1)
    c = random.randint(0, DIM - 1)
    while mat[r] != 0:
        r = random.randint(0, DIM - 1)
        c = random.randint(0, DIM - 1)
    mat[r] = 2


def get_current_state(mat):
    # if <WIN> in grid, you win
    for i in range(DIM):
        for j in range(DIM):
            if mat[i][j] == WIN:
                return 'WON'
    # if at least 1 empty cell, continue
    for i in range(DIM):
        for j in range(DIM):
            if not mat[i][j]:
                return 'CONTINUE'
    # if no empty cell, but legal move exists
    for i in range(DIM - 1):
        for j in range(DIM - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'CONTINUE'
    for j in range(DIM - 1):
        if mat[DIM - 1][j] == mat[DIM - 1][j + 1]:
            return 'CONTINUE'
    for i in range(DIM - 1):
        if mat[i][DIM - 1] == mat[i + 1][DIM - 1]:
            return 'CONTINUE'
    return 'LOST'
            

def compress(mat):
    'Compress grid before AND after each cell merging'
    is_changed = False
    new_mat = []
    for i in range(DIM):
        new_mat.append([0] * DIM)
    for i in range(DIM):
        pos = 0
        for j in range(DIM):
            if mat[i][j]:
                new_mat[i][pos] = mat[i][j]
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
            if mat[i][j] and mat[i][j] == mat[i][j + 1]:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                is_changed = True
    return mat, is_changed
