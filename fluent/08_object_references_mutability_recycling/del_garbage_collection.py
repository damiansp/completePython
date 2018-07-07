import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive) # True

del s1
print(ender.alive) # True!

s2 = 'spam'
print(ender.alive) # False
