import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

with open('data.bin', 'wb') as f:
    f.write(packed)

with open('data.bin', 'rb') as f:
    data = f.read()

print(data)
print(data[4:8])
print(list(data))
o = struct.unpack('>i4sh', data)
print(o)
