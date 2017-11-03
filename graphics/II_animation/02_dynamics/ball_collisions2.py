import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color

W, H = 600, 750
CYCLE_IN_MS = 40
TIME_INCR = 0.2
N_FRAMES = 1000
GRAVITY = 4
ELASTICITY_RANGE = (0.5, 0.95)
MAX_SPEED = 100
MAX_DIAMETER = 50
N_BALLS = 10


def main():
    root = Tk()
    root.title('Balls with trajectory traces')

    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=0)

    balls = [
        create_random_ball(ball)
        for ball in range(N_BALLS)]

    for i in range(N_FRAMES):
        for ball in balls:
            print(ball)
            ball = update_balls(canvas, ball, balls)
            print('   ', ball)
            
        canvas.update()
        canvas.after(CYCLE_IN_MS)
        canvas.delete('ball')
        
    root.mainloop()


def create_random_ball(ident):
    diameter = random.uniform(5, MAX_DIAMETER)
    return Ball(Point(random.uniform(0, W - diameter),
                      random.uniform(0, H -diameter)),
                Point(random.uniform(-MAX_SPEED, MAX_SPEED),
                      random.uniform(-MAX_SPEED, MAX_SPEED)),
                diameter,
                random_color(),
                random.uniform(ELASTICITY_RANGE[0], ELASTICITY_RANGE[1]),
                ident)


def update_balls(canvas, ball, balls):
    old_position = ball.position + Point(ball.diameter / 2, ball.diameter / 2)
    ball.velocity += Point(0, GRAVITY)
    ball.position += ball.velocity * TIME_INCR

    canvas.create_oval(
        ball.get_coords(), fill=ball.color, outline=ball.outline, tags='ball')
    canvas.create_line(
        old_position.as_list(),
        (ball.position + Point(ball.diameter / 2, ball.diameter / 2)).as_list(),
        fill=ball.color)
    ball = detect_wall_collision(ball)
    for b in balls:
        if ball.ident != b.ident:
            ball, b = detect_ball_collision(ball, b)
    return ball, balls
    

def detect_wall_collision(ball):
    if ball.position.x + ball.diameter >= W:
        ball.velocity.x = -ball.velocity.x * ball.elasticity
        ball.position.x = W - ball.diameter - 1
    elif ball.position.x < 1:
        ball.velocity.x = -ball.velocity.x * ball.elasticity
        ball.position.x = 1
    if ball.position.y + ball.diameter > H:
        ball.velocity.y = -ball.velocity.y * ball.elasticity
        ball.position.y = H - ball.diameter - 1
    elif ball.position.y < 1:
        ball.velocity.y = -ball.velocity.y * ball.elasticity
        ball.position.y = 1

    return ball


def detect_ball_collision(ball1, ball2):
    c1, r1 = ball1.get_cr()
    c2, r2 = ball2.get_cr()

    if c1.distance_from(c2) <= r1 + r2:
        ball1.velocity *= -1 * ball1.elasticity
        ball2.velocity *= -1 * ball2.elasticity
        ball1.position += ball1.velocity * TIME_INCR
        ball2.position += ball2.velocity * TIME_INCR
        
    return ball1, ball2


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

    def get_cr(self):
        radius = self.diameter / 2
        center = self.position + Point(radius, radius)
        return center, radius
        
    
if __name__ == '__main__':
    main()
