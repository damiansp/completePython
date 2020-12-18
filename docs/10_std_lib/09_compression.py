import zlib, bz2 # gzip, lzma, zipfile, tarfile


s = b'which witch has which witch\'s switch?'
print(len(s))

z = zlib.compress(s)
print('z:', len(z))

b = bz2.compress(s)
print('b:', len(b))

print(bz2.decompress(b))
