import array
import struct

cafe = bytes('café', encoding='utf_8')
print('cafe:', cafe)        # b'caf\xc3\xa9'
print(cafe[0])              # 99
print(cafe[0:1])            # 'c'

cafe_arr = bytearray(cafe)  
print('cafe_arr', cafe_arr) # bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])        # bytearray(b'\xa9')

print(bytes.fromhex('31 4B CE A9')) # b'1K\xce\xa9

numbers = array.array('h', [-2, -1, 0, 1, 2]) # h: short ints
print('numbers:', numbers) # array('h', [-2, -1, 0, 1, 2])

octets = bytes(numbers)
print('octets:', octets)   # b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'



# Structs and Memory views
# use memoryveiw and struct to inpsect GIF image header
fmt = '<3s3sHH' # < little-endian; 3s3s 2 seq of 3 bytes; HH 2 16-bit ints

with open('python.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))              # b'GIF87a \x00 \x00'
print(struct.unpack(fmt, header)) # (b'GIF', b'87a', 32, 32)

del(header)
del(img)
