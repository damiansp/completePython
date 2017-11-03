import math
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, random_color

W, H = 700, 500
CYCLE_IN_MS = 20
N_STEPS = 30


def main():
    root = Tk()
    root.title('Rotate 3D Cube')

    canvas = Canvas(root, width=W, height=H, background='white')
    canvas.grid(row=0, column=1)

    cube = construct_cube(Point3D(-100, -100, -100), 200)
    scale_vector = Point3D(2., 2., 1.)
    translate_vector = Point3D(450, 350, 0)
    angle_x, angle_y, angle_z = 0., 0., 0.

    for point in cube:
        point = point_setup(point, scale_vector, translate_vector)


    for i in range(N_STEPS):
        cube = rotate_shape(cube, 'x', angle_x)
        cube = rotate_shape(cube, 'y', angle_y)
        cube = rotate_shape(cube, 'z', angle_z)
        
        angle_x += 0.02
        angle_y += 0.005
        angle_z += 0.001

        draw_cube(canvas, cube)
        
    
    root.mainloop()



def construct_cube(front_bottom_left, length):
    p1 = front_bottom_left
    p2 = p1 + Point3D(length, 0, 0)
    p3 = p2 + Point3D(0, length, 0)
    p4 = p1 + Point3D(0, length, 0)
    p5 = p1 + Point3D(0, 0, length)
    p6 = p5 + Point3D(length, 0, 0)
    p7 = p6 + Point3D(0, length, 0)
    p8 = p5 + Point3D(0, length, 0)
    return [p1, p2, p3, p4, p5, p6, p7, p8]


def rotate_shape(shape, axis, degrees):
    for point in shape:
        rotate_point(axis, degrees)

    return shape


def rotate_point(point, axis, degrees):
    x, y, z = point.x, point.y. point.z
        
    if axis == 'y':
        x, y, z = y, z, x
    elif axis == 'z':
        x, y, z = z, x, y
        
    proj_length = math.sqrt(y**2 + z**2)
    angle = math.atan(y, z)
    y = proj_length * math.sin(angle + degrees)
    z = proj_length * math.cos(angle + degrees)

    if axis == 'y':
        y, z, x = x, y, z
    elif axis == 'z':
        z, x, y = x, y, z

    return Point(x, y, z)


def scale_point(point, scale_vector):
    point.x *= scale_vector.x
    point.y *= scale_vector.y
    point.z *= scale_vector.z

    return point


def point_setup(point, scale_vector, translate_vector):
    point = scale_point(point, scale_vector)
    point += translate_vector
    return point



class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_coords(self):
        return map(lambda point: point.as_list(), [self.p1, self.p2])


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


    def __str__(self):
        return '(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)
    
    def as_list(self):
        return [self.x, self.y, self.z]


if __name__ == '__main__':
    main()
