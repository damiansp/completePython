import itertools as it
import operator


data = [4, 5, 6, 2, 1, 9, 0, 7, 5, 8]
cumprod = list(it.accumulate(data, operator.mul))
print(cumprod)
cummax = list(it.accumulate(data, max))
print(cummax)

# Amortize a 5% loan of 1000 w 4 payments of 90
cashflows = [1000] + 4*[-90]
print(
    list(it.accumulate(cashflows, lambda bal, pmt: round(bal*1.05 + pmt, 2))))

               
a = ['a', 'b', 'c']
b = ['x', 'y', 'z']
for char in it.chain(a, b):
    print(char)


print(list(it.combinations('ABCD', 2)))   # AB, AC, AD, BC, CD
print(list(it.combinations(range(4), 3))) # 012, 013, 023, 123

print(list(it.combinations_with_replacement('ABCD', 2)))  # AA AB AC BB BC CC

print(list(it.compress('ABCDEF', [1, 0, 1, 1, 0, 1])))  # A C D F

counter = it.count(start=1976, step=10)
for _ in range(4):
    print(next(counter))  # 1976 1986 1996 2006


abcd_cycle = it.cycle('abcd')
for _ in range(10):
    print(next(abcd_cycle))


a = range(50)
a1 = it.dropwhile(lambda x: x < 30, a)
print(list(a1))


a2 = it.filterfalse(lambda x: x % 3 and x % 5, a)
print(list(a2))


print([k for k, g in it.groupby('AAAAABBBCCCCCDAANNN')]) # A B C D A N
print([list(g) for k, g in it.groupby('AAAAABBBCCCCCDAANNN')]) # AAAA, BBB...


data = 'ABCDEFG'
slicer = it.islice(data, 1, None, 2)  # iterable start stop step
print(list(slicer))  # BDF

print(list(it.pairwise(data)))  # AB BC CD DE..


print(list(it.permutations('ABCD', 2)))  # AB AC AD BA BC BD CA CB CD DA DB...
print(list(it.permutations(range(3), 3))) # 012 021 102 120 201 210

print(list(it.prodct('ABC', 'xy')))  # Ax Ay Bx By Cx Cy
print(list(it.product(range(2), repeat=3)))  # 000 001 010 011 100 101 110 111

