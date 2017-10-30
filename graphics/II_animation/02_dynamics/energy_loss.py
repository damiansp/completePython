import sys
from tkinter import *

sys.path.append('../../')
from util import Point

def main():
    root = Tk()
    root.title('Bouncing ball with energy loss on collision')

    W, H = 700, 500
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    CYCLE_IN_MS = 30
    N_FRAMES = 5000
    TIME_INCR = 0.2
    GRAVITY = 10
    ball_position = Point(15, 180)
    velocity = Point(20, 50)
    BALL_DIAMETER = 30
    COEF_RESTITUTION = 0.7
    COLOR = 'cyan'

    for i in range(N_FRAMES):
        velocity += Point(0, GRAVITY * TIME_INCR)
        ball_position += (velocity * TIME_INCR)
        canvas.create_oval(
            ball_position.as_list(),
            (ball_position + Point(BALL_DIAMETER, BALL_DIAMETER)).as_list(),
            fill=COLOR)
        ball_location, velocity = detect_collision(
            canvas, ball_position, BALL_DIAMETER, velocity, COEF_RESTITUTION)

        canvas.update()
        canvas.after(CYCLE_IN_MS)
        canvas.delete(ALL)
    
    root.mainloop()



def detect_collision(
    canvas, ball_location, ball_diameter, velocity, coef_restitution):
    
    width, height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()

    if ball_location.x + ball_diameter >= width or ball_location.x <= 0:
        velocity.x = -velocity.x * coef_restitution
    if ball_location.y + ball_diameter >= height or ball_location.y <= 0:
        velocity.y = -velocity.y * coef_restitution
        ball_location.y = height - ball_diameter

    return ball_location, velocity



if __name__ == '__main__':
    main()
