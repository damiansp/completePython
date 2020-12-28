import struct


with open('binary_file.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3): # first 3 file headers
    start += 14
    # <: little-endian; I: 4-byte unsigned; H: 2-byte unsigned
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filename_size, etra_size = fields
    start += 16
    filename = data[start:start + filename_size]
    start += filename_size
    print(filename, hex(crc32), comp_size, uncomp_size)
    start += extra_size + comp_size # skip to next header

