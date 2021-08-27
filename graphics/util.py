import math
import numpy as np

# Classes------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub_(self, other):
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
def rotate(shape, degrees, center=None):
    radians = math.radians(degrees)
    new = []

    if type(shape) == Point:
        shape = [shape]

    if not center:
        center = locate(shape)['center']

    for i in range(len(shape)):
        temp = Point(shape[i].x - center.x, shape[i].y - center.y)
        rad = math.atan2(temp.y, temp.x)
        mag = temp.distance_from(Point(0, 0))
        angle = radians + rad
        new_point = Point(mag * math.cos(angle) + center.x,
                          mag * math.sin(angle) + center.y)
        new.append(new_point)

    if len(shape) == 1:
        shape = shape[0]
        
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


def make_discrete_color_series(start_color, end_color, n_steps):
    '''Expects start and end as hex strings'''
    start_color, end_color = hex2rgb(start_color), hex2rgb(end_color)
    
    # deltas
    dr = (end_color[0] - start_color[0]) / (n_steps - 1)
    dg = (end_color[1] - start_color[1]) / (n_steps - 1)
    db = (end_color[2] - start_color[2]) / (n_steps - 1)
    
    #color_series_int = []
    color_series_hex = []
    
    for i in range(n_steps + 1):
        r = get_color_at_step(start_color[0], dr, i)
        g = get_color_at_step(start_color[1], dg, i)
        b = get_color_at_step(start_color[2], db, i)
        #color_series_int.append((r, g, b))
        
        if i < n_steps:
            color_series_hex.append('#%02x%02x%02x' % (r, g, b))
        else:
            color_series_hex.append('#%02x%02x%02x' % end_color)
            
    return color_series_hex


def get_color_at_step(start_color, delta, step):
    color = start_color + step * delta
    color = color if color > 0 else 0
    color = color if color < 255 else 255
    return int(color)
                



# Shapes-------------------------------------------------------------------
def make_regular_poly(n_sides, center, radius):
    vertex = center + Point(0, -radius)
    degrees_per_vertex = 360 / n_sides
    poly = [vertex]

    for i in range(n_sides - 1):
        vertex = rotate(vertex, degrees_per_vertex, center)
        vertex_int = Point(int(vertex[0].x), int(vertex[0].y))
        poly.append(vertex_int)

    return poly
