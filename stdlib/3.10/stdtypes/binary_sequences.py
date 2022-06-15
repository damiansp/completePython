# Bytes, bytearrays, memoryviews


# Bytes
bytestr = b'any old ascii string here'
zero_filled = bytes(10)
from_hex = bytes.fromhex('2Ef0 F1f2  ')
print(from_hex)
to_hex = b'.\xf0\xf1\xf2'.hex()
print(to_hex)


# Bytearray (mutable counterpart to bytes)
from_hex = bytearray.fromhex('2Ef0 f1F2  ')
to_hex = bytearray(b'.\xf0\xf1\xf2').hex()
print(from_hex)
print(to_hex)


# Ops on bytes/bytearray
a = b'abc'
b = a.replace(b'a', b'z')
print(b)

b = b'my itty bitty byte string'
print(b.count(b'b'))
# 3.9+
#print(b.removeprefix(b'my '))
print(b.find(b'tt'))
print(b' '.join([b'one', b'two', b'three']))
print(b.replace(b't', b'g'))
