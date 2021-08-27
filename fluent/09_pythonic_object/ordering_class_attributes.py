from vector_immutable import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))        # 17

v1.typecode = 'f'        # instance var exists as well as class var
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))        # 9
print(Vector2d.typecode) # d
