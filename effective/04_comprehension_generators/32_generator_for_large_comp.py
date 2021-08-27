val = [len(x) for x in open('my_numbers.txt')]
print(val) # but what if it is long enough to cause memory issues?


it = (len(x) for x in open('my_numbers.txt'))
print(it) # <generator object ...>
print(next(it)) # 3


# can also compose generators:
it = (len(x) for x in open('my_numbers.txt'))
roots = ((x, x**0.5) for x in it)
print(next(roots)) # (3, 1.73205...) # BOTH generators advance

