import random


DIM = 4


def start_game():
    mat = []
    for in range(DIM):
        mat.append([0] * DIM)
    print_controls()
    add_new_2(mat)
    return mat


def print_controls():
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")


def add_new_2(mat):
    'Add a new 2 at random in any empty grid cell'
    # code appears to be faulty
    r = random.randint(0, DIM - 1)
    c = random.randint(0, DIM - 1)
    while mat[r] != 0:
        r = random.randint(0, DIM - 1)
        c = random.randint(0, DIM - 1)
    mat[r] = 2
