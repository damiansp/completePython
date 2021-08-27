from functools import reduce
from operator import add


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(string):
    return string[::-1]

print(reverse('testing'))
print(sorted(fruits, key=reverse))

# NOTE py 2: apply(f, args, kwargs) ->
#      py 3: f(*args, **kwargs)



# Modern replacements for map, filter, reduce
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

fact = factorial

print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

print(reduce(add, range(100))) # better as:
print(sum(range(100)))

# Anonymous functions
print(sorted(fruits, key=lambda word: word[::-1]))


