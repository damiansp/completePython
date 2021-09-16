from datetime import date
from math import cos, radians
import re


a = [1, 1, 2, 3, 5, 8]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if (n := len(a)) > 10:
    print(f'List too long to print ({n} items)')
else:
    print(a)

if (n := len(b)) > 10:
    print(f'List too long to print ({n} items)')
else:
    print(b)


discount = 0.
advertisement = 'get a 25% discount'
if (mo := re.search(r'(\d+)% discount', advertisement)):
    discount = float(mo.group(1)) / 100.
    print('Discount:', discount)


#while (block := f.read(256)) != '':
#    process(block)

#[clean_name.title() for name in names
# if (clean_name := normaliz('NFC', name)) in allowed names]


# Positional-Only Parameters
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(1, 2, 3, d=40, e=50, f=60)         # ok
# f(1, b=20, c=30, d=40, e=50, f=60) # NO - b cannot be kwarg
# f(1, 2, 3, 4, 5, f=60)             # NO - e must be kwarg


def divmod(a, b, /):
    'Emulate builtin (C) divmod'
    return (a // b, a % b)

# note builtin len() is
#def len(obj, /)
#len(obj='hello') not allowed... only len('hello')


# allows name of arg 'dist' to be changed w/o breaking code
def quantiles(dist, /, *, n=4, method='exclusive'):
    pass # ...


def g(a, b, /, **kwargs):
    print(a, b, kwargs)

g(10, 20, a=1, b=2, c=3) # kwarg a distinct from param a


# f-string =
user = 'eric idle'
member_since = date(1975, 7, 31)
print(f'{user=} {member_since=}')

delta = date.today() - member_since
print(f'{user=!s} {delta.days=:,d}')

theta = 30
print(f'{theta=} {cos(radians(theta))=:.3f}')

    
