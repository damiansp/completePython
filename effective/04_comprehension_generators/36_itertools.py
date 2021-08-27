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
vals = list(range(1, 11))
first_five = itertools.islice(vals, 5)
print('First five:', list(first_five)) # [1 2 3 4 5]
middle_odds = itertools.islice(vals, 2, 8, 2)
print('Middle odds:', list(middle_odds)) # [3 5 7]

lt7 = lambda x: x < 7
it = itertools.takewhile(lt7, vals)
print(list(it)) # [1 2 3 4 5 6]

it = itertools.dropwhile(lt7, vals)
print(list(it)) # [7 8 9 10]

evens = lambda x: x % 2 == 0
filter_res = filter(evens, vals)
print('Filter:      ', list(filter_res))       # [2 4 6 8 10]
filter_false_res = itertools.filterfalse(evens, vals)
print('Filter false:', list(filter_false_res)) # [1 3 5 7 9]

sum_reduce = itertools.accumulate(vals)
print('Cum Sum:', list(sum_reduce)) # [1 3 6 10 15 21 28 36 45 55]

def sum_mod20(first, second):
    out = first + second
    return out % 20

mod_reduce = itertools.accumulate(vals, sum_mod20)
print('Modulo:', list(mod_reduce)) # [1 3 6 10 15 1 8 16 5 15]
# 1 2
#   3 -> 3; + 3 = 6 -> 6; + 4 = 10 -> 10; + 5 = 15 -> 15; +6 = 21 % 20 = 1...

single = itertools.product([1, 2], repeat=2)
print('Single:', list(single)) # [(1 1) (1 2) (2 1) (2 2)]

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple)) # [(1 a) (1 b) (2 a) (2 b)]

it = itertools.permutations([1, 2, 3], 2)
print(list(it)) # [(1 2) (1 3) (2 1) (2 3) (3 1) (3 2)]

it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it)) # [(1 2) (1 3) (1 4) (2 3) (2 4) (3 4)]

it = itertools.combinations_with_replacement([1, 2, 3], 2)
print(list(it)) # [(1 1) (1 2) (1 3) (2 2) (2 3) (3 3)]

