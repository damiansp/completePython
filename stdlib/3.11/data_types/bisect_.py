from bisect import bisect, bisect_left, bisect_right, insort
from collections import namedtuple
from operator import attrgetter
from pprint import pprint


# Searching Sorted Lists
def index(a, x):
    'Find leftmost value in a exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value < x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value <= x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value > x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    'Find leftmost value >= x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]


Movie = namedtuple('Movie', ('name', 'released', 'director'))
movies = [
    Movie('Jaws', 1975, 'Spielberg'),
    Movie('Titanic', 1997, 'Cameron'),
    Movie('The Birds', 1963, 'Hitchcock'),
    Movie('Aliens', 1986, 'Scott')]
by_year = attrgetter('released')
movies.sort(key=by_year)
print(movies[bisect(movies, 1960, key=by_year)])  # first movie released > 1960

# insert movie while maintaining sort ored=
romance = Movie('Love Story', 1970, 'Hiller')
insort(movies, romance, key=by_year)
pprint(movies)


data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])  # or use operator.itemgetter(1)
keys = [r[1] for r in data]    # precompute list of keys
print(data[bisect_left(keys, 0)])  # black, 0
print(data[bisect_left(keys, 5)])  # red, 5
print(data[bisect_left(keys, 8)])  # yellow, 8
