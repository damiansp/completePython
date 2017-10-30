import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color

def main():
    root = Tk()
    root.title('Balls with trajectory traces')

    W, H = 600, 750
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=0)

    CYCLE_IN_MS = 80
    TIME_INCR = 0.2
    N_FRAMES = 1000
    GRAVITY = 4
    ELASTICITY_RANGE = (0.5, 0.95)
    MAX_SPEED = 100
    MAX_DIAMETER = 50
    N_BALLS = 15

    balls = [
        create_random_ball(W - MAX_DIAMETER,
                           H - MAX_DIAMETER,
                           MAX_SPEED,
                           MAX_DIAMETER,
                           ELASTICITY_RANGE,
                           ball)
        for ball in range(N_BALLS)]

    for i in range(N_FRAMES):
        for ball in balls:
            print(ball)
            ball = update_ball(canvas, ball, GRAVITY, TIME_INCR)
            print('   ', ball)
            
        canvas.update()
        canvas.after(CYCLE_IN_MS)
        canvas.delete('ball')
        
    root.mainloop()


def create_random_ball(
    max_width, max_height, max_speed, max_diameter, elasticity_range, ident):
    
    diameter = random.uniform(5, max_diameter)
    return Ball(Point(random.uniform(0, max_width - diameter),
                      random.uniform(0, max_height -diameter)),
                Point(random.uniform(-max_speed, max_speed),
                      random.uniform(-max_speed, max_speed)),
                diameter,
                random_color(),
                random.uniform(elasticity_range[0], elasticity_range[1]),
                ident)


def update_ball(canvas, ball, gravity, time_incr):
    old_position = ball.position + Point(ball.diameter / 2, ball.diameter / 2)
    ball.velocity += Point(0, gravity)
    ball.position += ball.velocity * time_incr

    canvas.create_oval(
        ball.get_coords(), fill=ball.color, outline=ball.outline, tags='ball')
    canvas.create_line(
        old_position.as_list(),
        (ball.position + Point(ball.diameter / 2, ball.diameter / 2)).as_list(),
        fill=ball.color)
    ball = detect_collision(canvas, ball)
    return ball
    

def detect_collision(canvas, ball):
    width, height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()

    if ball.position.x + ball.diameter >= width:
        ball.velocity.x = -ball.velocity.x * ball.elasticity
        ball.position.x = width - ball.diameter - 1
    elif ball.position.x < 1:
        ball.velocity.x = -ball.velocity.x * ball.elasticity
        ball.position.x = 1
    if ball.position.y + ball.diameter > height:
        ball.velocity.y = -ball.velocity.y * ball.elasticity
        ball.position.y = height - ball.diameter - 1
    elif ball.position.y < 1:
        ball.velocity.y = -ball.velocity.y * ball.elasticity
        ball.position.y = 1

    return ball


class Ball:
    def __init__(self, position, velocity, diameter, color, elasticity, ident):
        self.position = position
        self.velocity = velocity
        self.diameter = diameter
        self.color = color
        self.outline = random_color()
        self.elasticity = elasticity
        self.ident = ident

    def __str__(self):
        return (
            'Ball: %s\n (%.2f, %.2f); vel: (%.2f, %.2f); d: %.2f; elas: %.2f)'
            % (self.ident, self.position.x, self.position.y,
               self.velocity.x, self.velocity.y,
               self.diameter, self.elasticity))
        
    def get_coords(self):
        self.bottom_right = self.position + Point(self.diameter, self.diameter)
        return (self.position.as_list(), self.bottom_right.as_list())


    def set_position(self, point):
        self.position = point
        
    
if __name__ == '__main__':
    main()
