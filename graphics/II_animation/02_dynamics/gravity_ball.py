import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color

def main():
    root = Tk()
    root.title('Gravity')

    W, H = 600, 750
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    GRAVITY = Point(0, 6)
    CYCLE_IN_MS = 30
    N_STEPS = 300
    ABSORB = 0.85
    N_BALLS = 100
    MAX_DIAMETER = 40
    
    balls = [make_random_ball(W, H, MAX_DIAMETER) for ball in range(N_BALLS)]
    
    for step in range(N_STEPS):
        for ball in balls:
            draw(canvas, ball)
            ball.move()
            ball = add_gravity(GRAVITY, ball)
            collision = check_collision(ball, canvas)

            if collision['is_collision']:
                ball = collide(ball, canvas, collision['side'], ABSORB)
                print('Collision!')

        canvas.update()
        canvas.after(CYCLE_IN_MS)
        canvas.delete(ALL)
                           
    root.mainloop()


def make_random_ball(max_x, max_y, max_diameter):    
    location = Point(random.uniform(0, max_x), random.uniform(0, max_y))
    diameter = random.uniform(5, max_diameter)
    initial_acceleration = Point(random.uniform(0, 20), random.uniform(-20, 0))
    ball = Ball(location, diameter, initial_acceleration)
    ball.set_color(random_color())
    ball.set_outline(random_color())
    return ball


def add_gravity(gravity, obj):
    obj.acceleration += gravity
    return obj


def check_collision(ball, canvas):
    width, height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    is_collision = False
    collision_side = None
    
    if ball.location.x <= 0:
        is_collision = True
        collision_side = 'left'
    if ball.location.x + ball.diameter >= width:
        is_collision = True
        collision_side = 'right'
    if ball.location.y <= 0:
        is_collision = True
        collision_sixe = 'top'
    if ball.location.y + ball.diameter >= height:
        is_collision = True
        collision_side = 'bottom'

    return {'is_collision': is_collision, 'side': collision_side}


def collide(ball, canvas, collision_side, absorb=0):
    width, height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()

    # Collision may have occurred on previous step, but the ball may not yet
    # have cleared the wall, which will trigger "another" collision.  If so, do
    # nothing
    if (collision_side == 'right' and ball.acceleration.x < 0 or
        collision_side == 'left' and ball.acceleration.x > 0 or
        collision_side == 'bottom' and ball.acceleration.y < 0 or
        collision_side == 'top' and ball.acceleration.y > 0):
        return ball
        
    if collision_side in ['left', 'right']:
        factor = Point(-1, 1)
    else:
        factor = Point(1, -1)
    ball.acceleration = Point(ball.acceleration.x * factor.x,
                              ball.acceleration.y * factor.y)
    if collision_side == 'top':
        ball.acceleration.y *= absorb
    elif collision_side == 'bottom':
        ball.acceleration.y *= absorb
    elif collision_side == 'left':
        ball.acceleration.x *= absorb
    elif collision_side == 'right':
        ball.acceleration.x *= absorb

    return ball


def draw(canvas, ball):
    canvas.create_oval(
        ball.get_coords_as_list(), fill=ball.color, outline=ball.outline)




class Ball:
    def __init__(self, location, diameter, acceleration):
        '''location is the upper-left corner of the bounding box'''
        self.location = location
        self.diameter = diameter
        self.acceleration = acceleration
        self.coords = self.set_coords()

    def __str__(self):
        return ('location: %s, acceleration: %s'
                % (self.location, self.acceleration))
    def set_coords(self):
        return [self.location,
                self.location + Point(self.diameter, self.diameter)]

    def get_coords_as_list(self):
        return [point.as_list() for point in self.coords]

    def set_color(self, color):
        self.color = color

    def set_outline(self, color):
        self.outline = color

    def move(self, steps=1):
        self.coords = [point + self.acceleration for point in self.coords]
        self.location = self.coords[0]



if __name__ == '__main__':
    main()
