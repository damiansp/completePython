import array
from   ctypes import BigEndianStructure, c_long
import struct


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

m.release()
try:
    print(m[0])
except ValueError as e:
    print(e)  # operation forbiden on released memoryview object

# can also use ctxt mgr, e.g.:
with memoryview(b'abc') as m:
    print(m[0])
    # ...
    
try:
    print(m[0])
except ValueError as e:
    print(e)  # operation forbiden on released memoryview object

a = array.array('l', [1, 2, 3])
x = memoryview(a)
print(x.format)    # 'l'
print(x.itemsize)  # 8 (bytes per elem)
print(len(x))      # 3
print(x.nbytes)    # 24
y = x.cast('B')
print(y.format)    # 'B'
print(y.itemsize)  # 1
print(len(y))      # 24
print(y.nbytes)    # 24

b = bytearray(b'zyz')
x = memoryview(b)
try:
    x[0] = b'a'
except TypeError as e:
    print(e)  # invalid type for format 'B'
y = x.cast('c')
y[0] = b'a'
print(b)      # bytearray(b'ayz')

buf = struct.pack('i' * 12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2, 2, 3])
print(y.tolist())  # [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
print(y.format)    # 'i'
print(y.itemsize)  # 4
print(len(y))      # 2
print(y.nbytes)    # 48
z = y.cast('b')
print(z.itemsize)  # 1
print(len(z))      # 48

buf = struct.pack('L' * 6, *list(range(6)))
x = memoryview(buf)
y = x.cast('L', shape=[2, 3])
print(len(y))      # 2
print(y.nbytes)    # 48
print(y.tolist())  # [[0, 1, 2], [3, 4, 5]]

b = bytearray(b'xyz')
m = memoryview(b)
print(m.obj is b)  # True (b is the object m references)

a = array.array('i', [1, 2, 3, 4, 5])
m = memoryview(a)
print(len(m))            # 5
print(m.nbytes)          # 20
y = m[::2]
print(len(y))            # 3
print(y.nbytes)          # 12
print(len(y.tobytes()))  # 12

buf = struct.pack('d' * 12, *[1.5 * x for x in range(12)])
x = memoryview(buf)
y = x.cast('d', shape=[3, 4])
print(y.tolist())  # [[0., 1.5, 3., 4.5], [6., 7.5, 9., 10.5], [12., ...,16.5]]
print(len(y))      # 3
print(y.nbytes)    # 96

m = memoryview(array.array('H', [32_000, 32_001, 32_002]))
print(m.itemsize)  # 2 (bytes per elem)
print(m[0])        # 32000
print(struct.calcsize('H') == m.itemsize)  # True

