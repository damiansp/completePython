import array
from ctypes import BigEndianStructure, c_long


# memoryview() is a *reference* to an object, not a copy or the obj itself
v = memoryview(b'abcefg')
print(v[1])    # 98
print(v[-1])   # 103
print(v[1:4])  # <memory at 0x...>
print(bytes(v[1:4]))  # b'bce'

a = array.array('l', [-1111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(m[0])             # -1111111
print(m[::2].tolist())  # [-1111111, -33333333]

data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)  # False
v[0] = ord(b'z')
v[1:4] = b'123'
print(data)        # bytearray(b'z123fg')
try:
    v[2:3] = b'spam'
except Exception as e:
    # memoryview assignment: lvalue and rvalue have different structures
    print(e)       
v[2:6] = b'spam'
print(data)        # bytearray(b'z1spam')


# hash(m) def eq = hash(m.tobytes())
v = memoryview(b'abcefg')
print(hash(v) == hash(b'abcefg'))  # True


a = array.array('I', [1, 2, 3, 4, 5])
b = array.array('d', [1., 2., 3., 4., 5.])
c = array.array('b', [5, 3, 1])
x = memoryview(a)
y = memoryview(b)
print(x == a == y == b)  # True
print(x.tolist() == a.tolist() == y.tolist() == b.tolist())  # True
z = y[::-2]
print(z == c)                    # True
print(z.tolist() == c.tolist())  # True


class BEPoint(BigEndianStructure):
    _fields_ = [('x', c_long), ('y', c_long)]


point = BEPoint(100, 200)
a = memoryview(point)
b = memoryview(point)
print(a == point)  # False
print(a == b)      # False


m = memoryview(b'abc')
print(m.tobytes())  # b'abc'
print(bytes(m))     # b'abc'

print(m.hex())     # 616263 (2 hex digits per byte)
print(m.tolist())  # [97, 98, 99]

a = array.array('d', [1.1, 2.2, 3.3])
print(a)           # array('d', [1.1, 2.2, 3.3])
m = memoryview(a)
print(m.tolist())  # [1.1., 2.2, 3.3]

m = memoryview(bytearray(b'abc'))
mm = m.toreadonly()
print(mm.tolist())  # [97, 98, 99]
try:
    mm[0] = 42
except TypeError as e:
    print(e)        # cannot modify read-only memory
m[0] = 43
print(mm.tolist())  # [43, 98, 99]
