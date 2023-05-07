from enum import Enum
import json


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(type(Color.RED))  # <enum 'Color'>
print(isinstance(Color.RED, Color))  # True
print(Color.RED.name)   # RED
print(Color.RED.value)  # 1
print(Color.RED in Color)  # True
print(Color.RED == 1)      # False
print(Color.RED is 1)      # False

rgb = {
    Color.RED: '#ff0000',
    Color.GREEN: '#00ff00',
    Color.BLUE: '#0000ff'}

print(Color(1))
prin(Color['RED'] == Color(1))  # True

for color in Color:
    print(color)
print(list(Color))

# Errors:
#Color['YELLOW'] = 3
#Color.RED.value = 100


class Color(Enum):
    pass


class RGB(Color):
    RED = 1
    GREEN = 2
    BLUE = 3


class RGBA(RGB):
    ALPHA = 4


class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'


response = '{"status": "fulfilled"}'
data = json.loads(response)
status = data['status']
print(ResponseStatus(status))
