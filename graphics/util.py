import math
import numpy as np

# Classes------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Point(self.x * factor, self.y * factor)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance_from(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def as_list(self):
        return [self.x, self.y]
    

# Mappings-----------------------------------------------------------------
def rotate_point(center, point, degrees):
    rad = math.radians(degrees)
    a_rad = math.atan2((point.y - center.y), (point.x - center.x))
    a_len = center.distance_to(point)
    rad += a_rad
    new_x = a_len * math.cos(rad)
    new_y = a_len * math.sin(rad)
    return Point(new_x, new_y)


def rotate_shape(shape, center, degrees):
    radians = math.radians(degrees)
    new = []

    for i in range(len(shape)):
        temp = Point(shape[i].x - center.x, shape[i].y - center.y)
        rad = math.atan2(temp.y, temp.x)
        mag = temp.distance_from(Point(0, 0))
        angle = radians + rad
        new_point = Point(mag * math.cos(angle) + center.x,
                          mag * math.sin(angle) + center.y)
        new.append(new_point)
    return new


def translate_shape(shape, x, y):
    for i in range(len(shape)):
        shape[i] += Point(x, y)
    return shape


def rescale(shape, factor):
    center = locate(shape)['center']
    rescaled = []
    
    for i in range(len(shape)):
        x_offset = shape[i].x - center.x
        y_offset = shape[i].y - center.y
        new_x = center.x + factor * x_offset
        new_y = center.y + factor * y_offset
        rescaled.append(Point(new_x, new_y))

    return rescaled


def locate(shape):
    '''Get shape's bounding box (bb) and center'''
    xmin = xmax = shape[0].x
    ymin = ymax = shape[0].y

    for point in shape:
        if point.x < xmin:
            xmin = point.x
        if point.x > xmax:
            xmax = point.x
        if point.y < ymin:
            ymin = point.y
        if point.y > ymax:
            ymax = point.y

    bb = [Point(xmin, ymin), Point(xmax, ymax)]
    center = Point(int(round((xmin + xmax) / 2)), int(round((ymin + ymax) / 2)))
    return {'bb': bb, 'center': center}
                                                      
    

# Color stuff--------------------------------------------------------------
def rgb2hex(r, g, b, max_val=255):
    if max_val != 255:
        def rescale(x):
            return 255 * x / max_val

        r = rescale(r)
        g = rescale(g)
        b = rescale(b)

    r = int(round(r))
    g = int(round(g))
    b = int(round(b))

    return '#%02x%02x%02x' %(r, g, b)


def hex2rgb(hex_color):
    rgb = []

    for i in range(3):
        color_channel = hex_color[2*i + 1 : 2*i + 3]
        rgb.append(int(color_channel, 16))

    return tuple(rgb)

    
def random_color():
    digits = list('0123456789abcdef')
    return '#' + ''.join([np.random.choice(digits) for i in range(6)])
