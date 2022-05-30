class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p.__dict__)
p.z = 42
print(p.__dict__)
