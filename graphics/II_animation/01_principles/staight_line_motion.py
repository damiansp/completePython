import sys
from tkinter import *

sys.path.append('../../')
from util import Point

def main():
    root = Tk()
    root.title('Ball')

    W, H = 700, 700
    PAD = 10
    DIAMETER = 25
    CYCLE_MS = 15
    
    canvas = Canvas(root, width=W, height=H, background='white')
    canvas.grid(row=0, column=1)

    ball = [Point(PAD, PAD),
            Point(PAD + DIAMETER, PAD + DIAMETER)]
    ball_box = [point.as_list() for point in ball]
    shift = Point(1, 1)

    canvas.create_oval(ball_box, fill='green')


    for i in range(1, 500):
        ball = [point + shift for point in ball]
        ball_box = [point.as_list() for point in ball]
        canvas.create_oval(ball_box, fill='green')
        canvas.update()
        canvas.after(CYCLE_MS)
        canvas.delete(ALL)

    root.mainloop()


if __name__ == '__main__':
    main()
