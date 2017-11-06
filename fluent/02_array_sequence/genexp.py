import array

symbols = '$¢£¥€¤'
print((ord(s) for s in symbols))
print(tuple(ord(s) for s in symbols))

ords = (ord(s) for s in symbols)
print(next(ords))

a = array.array('I', (ord(s) for s in symbols))
print(a)

colors = ['red', 'blue']
sizes = list('SML')
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)


