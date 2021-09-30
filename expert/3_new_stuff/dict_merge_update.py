a1 = [1, 2, 3]
a2 = [4, 5, 6]
a = a1 + a2
print(a) # [1, 2, 3, 4, 5, 6]

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t = t1 + t2
print(t) # (1, 2, 3, 4, 5, 6)

val = a1.copy()
val += a2
print(val) # same as a

val = t1[:]
val += t2
print(val) # same as t

s1 = {1, 2, 3}
s2 = {1, 4}
inter = s1 & s2
print(inter) # {1}

union = s1 | s2
print(union) # {1, 2, 3, 4}

sdiff = s1 - s2
print(sdiff) # {2, 3}

xor = s1 ^ s2
print(xor) # {2, 3, 4}


# 3.9+
#d1 = {'a': 1, 'b': 2}
#d2 = {'a': 10, 'c': 30}
#upd = d1 | d2
#print(upd)
