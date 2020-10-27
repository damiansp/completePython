import itertools


# Linking
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it)) # [1 2 3 4 5 6]

it = itertools.repeat('hi', 3)
print(list(it)) # [hi hi hi]

it = itertools.cycle([1, 2])
res = [next(it) for _ in range(10)]
print(res) # [1 2 1 2 1 2 1 2 1 2]

it1, it2, it3 = itertools.tee(['i', 'ii'], 3)
print(list(it1)) # [i ii]
print(list(it2)) # [i ii]
print(list(it3)) # [i ii]

keys = ['i', 'ii', 'iii']
vals = [1, 2]
normal = list(zip(keys, vals))
print('zip:', normal) # [(i 1), (ii 2)] # iii is dropped

it = itertools.zip_longest(keys, vals, fillvalue='nonesuch')
longest = list(it)
print('zip_longest:', longest) # [(i 1), (ii 2), (iii nonesuch)]



# Filtering
