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
