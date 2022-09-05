import pyximport
pyximport.install()

from iterator_support import I


i = I()
s = 0
for x in i:
    s += x

print('s:', s)


it = iter(I())
print(next(it))
print(next(it))

