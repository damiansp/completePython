from collections import ChainMap


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
d1 = {'a': 1, 'b': 2}
d2 = {'a': 10, 'c': 30}
#upd = d1 | d2
#print(upd)

#d1 |= d2
#print(d1)

upd = {**d1, **d2} # d2 overwrites d1
print(upd) 


user_acct = {'iban': 'fwif9098wf98n', 'type': 'account'}
user_profile = {'name': 'Bob Dobolina', 'type': 'profile'}
user = ChainMap(user_acct, user_profile)
print(user)
print(user['iban'])
print(user['name'])
print(user['type']) # account (not overwritten)

user_profile['name'] = 'Abe Linky'
print(user['name']) # updates here too

user['age'] = 33
user['type'] = 'extension'
print(user_acct) # age appended and type = extension
print(user_acct) # here too


