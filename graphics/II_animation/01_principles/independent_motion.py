import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color

def main():
    root = Tk()
    root.title('')

    W, H = 600, 750
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    PAD = 20
    CYCLE_MS = 10
    N_BALLS = 100

    balls = [make_ball_with_trajectory(W, H) for ball in range(N_BALLS)]

    for i in range(500):
        for ball in balls:
            ball['coordinates'] = [point.as_list() for point in ball['ball']]
            canvas.create_oval(
                ball['coordinates'], fill=ball['color'], outline='white')
            ball['ball'] = [point + ball['trajectory']
                            for point in ball['ball']]

        canvas.update()
        canvas.after(CYCLE_MS)
        canvas.delete(ALL)
        
    root.mainloop()


def make_ball_with_trajectory(max_width, max_height):
    diameter = random.uniform(5, 35)
    p1 = Point(random.uniform(0, max_width), random.uniform(0, max_height))
    ball = [p1, p1 + Point(diameter, diameter)]
    trajectory = Point(random.choice([-3, -2, -1, 1, 2, 3]),
                       random.choice([-3, -2, -1, 1, 2, 3]))
    color = random_color()

    return {'ball': ball, 'trajectory': trajectory, 'color': color}
               



if __name__ == '__main__':
    main()
