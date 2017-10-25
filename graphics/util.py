import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance_from(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def as_list(self):
        return [self.x, self.y]
    

def rotate_point(center, point, degrees):
    rad = math.radians(degrees)
    a_rad = math.atan2((point.y - center.y), (point.x - center.x))
    a_len = center.distance_to(point)
    rad += a_rad
    new_x = a_len * math.cos(rad)
    new_y = a_len * math.sin(rad)
    return Point(new_x, new_y)


def rotate_shape(shape, center, degrees):
    '''Expects shape is a list of Points'''
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

    
