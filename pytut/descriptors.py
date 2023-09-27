import os


# non-data descriptor
class FileCount:
    def __get__(self, instance, owner):
        print('__get__ called')
        return len(os.listdir(instance.path))


class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path


folder = Folder('/')
print('file count:', folder.count)

# Python checks this first, so if found, does not use descriptor
folder.__dict__['count'] = 100  
print('file count:', folder.count)


# data descriptor
class Coordinate:
    def __get__(self, instance, owner):
        print('__get__ called')

    def __set__(self, instance, value):
        print('__set__ called')


class Point:
    x = Coordinate()
    y = Coordinate()


p = Point()
p.x = 10
print(p.x)
