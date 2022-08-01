from collections import namedtuple
from struct import *


print(pack('hhl', 1, 2, 3))  # pack values 1, 2, 3 as short, short, long
#print(unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(calcsize('hhl'))

record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)

Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(unpack('<10sHHb', record))


print(pack('ci', b'*', 0x12131415))
print(pack('ic', 0x12131415, b'*'))
print(calcsize('ci'), calcsize('ic'))

print(pack('llh0l', 1, 2, 3))
