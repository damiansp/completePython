a = [1, 2, 3]
b = a
a.append(4)
print(b)


class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
#y = Gizmo() * 10 # ERROR, but shows that obj created before var assigned
print(dir())


