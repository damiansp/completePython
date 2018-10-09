import itertools
import operator


def vowel(c):
    return c.lower() in 'aeiou'

word = 'Aardvark'
print(list(filter(vowel, word)))                          # [A a a]
print(list(itertools.filterfalse(vowel, word)))           # [r d v r k]
print(list(itertools.dropwhile(vowel, word)))             # [r d v a r k]
print(list(itertools.takewhile(vowel, word)))             # [A a]
print(list(itertools.compress(word, (1, 0, 1, 1, 0, 1)))) # [A r d a]
print(list(itertools.islice(word, 4)))                    # [A a r d]
print(list(itertools.islice(word, 4, 7)))                 # [v a r]
print(list(itertools.islice(word, 1, 7, 2)))              # [a d a]


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))                     # [5 9 11 19 ...]
print(list(itertools.accumulate(sample, min)))                # [5 4 2 2 2...]
print(list(itertools.accumulate(sample, max)))                # [5 5 5 8 8...]
print(list(itertools.accumulate(sample, operator.mul)))       # [5 20 40 320...]
print(list(itertools.accumulate(range(1, 11), operator.mul))) # [1 2 6 24...]


print(list(enumerate('abcdefg', 1))) # [(1 a) (2 b) (3 c)...]
print(list(map(operator.mul, range(11), range(11)))) # [0 1 4 9 ...]
print(list(map(operator.mul, range(11), [2, 4, 8]))) # [0 4 16]
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
# [(0 2) (1 4) (2 8)]
print(list(itertools.starmap(operator.mul, enumerate('abcde', 1))))
# [a bb ccc dddd eeeee]
print(list(itertools.starmap(
    lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))


# merging generators
print(list(itertools.chain('ABC', range(2)))) # [A B C 0 1]
print(list(itertools.chain(enumerate('ABC')))) # [(0 A) (1 B) (2 C)]
print(list(itertools.chain.from_iterable(enumerate('ABC')))) # [0 A 1 B 2 C]
print(list(zip('ABC', range(5)))) # [(A 0) (B 1) (C 2)]
print(list(itertools.zip_longest('ABC', range(5))))
# [(A 0) (B 1) (C 2) (None 3) (None 4)]
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))
# [(A 0) (B 1) (C 2) (? 3) (? 4)]


print(list(itertools.product('ABC', range(2)))) # [(A 0) (A 1) (B 0) (B 1) ...]
suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))
print(list(itertools.product('ABC'))) # [(A,) (B,) (C,)]
print(list(itertools.product('ABC', repeat=2))) # [(A A) (A B) (A C) (B A)...]
print(list(itertools.product(range(2), repeat=3))) # [(0 0 0) (0 0 1) (0 1 0)..]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row) # (A 0 A 0)\(A 0 A 1)\(A 0 B 0)...


ct = itertools.count()
print(next(ct)) # 0
print(next(ct), next(ct), next(ct)) # (1, 2, 3)
print(list(itertools.islice(itertools.count(1, 0.3), 3))) # [1 1.3 1.6]
cy = itertools.cycle('ABC')
print(next(cy)) # A
print(list(itertools.islice(cy, 7))) # [B C A B C A B]
rp = itertools.repeat(7)
print(next(rp), next(rp)) # (7 7)
print(list(itertools.repeat(8, 4))) # [8 8 8 8]
print(list(map(operator.mul, range(11), itertools.repeat(5)))) # [0 5 10 15...]
      
