t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = t1[:]
print(t2 is t1) # True 
print(t3 is t2) # True


t4 = (1, 2, 3)
print(t4 is t1) # False

s1 = 'abc'
s2 = 'abc'
print(s2 is s1) # True

me = 'damian'
you = 'damian'
print(me is you) # True
