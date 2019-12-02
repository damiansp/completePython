from collections import namedtuple


red = lambda color: color[0]
green = lambda color: color[1]
blue = lambda color: color[2]

mycolor = (127, 222, 255, 'mycolor')
print(red(mycolor))

Color = namedtuple('Color', ('red', 'green', 'blue', 'name'))
mycolor = Color(127, 222, 255, 'mycolor')
print(mycolor.red)
