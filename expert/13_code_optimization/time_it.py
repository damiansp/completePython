import timeit

from my_app import light


print(timeit.timeit(light, number=1000))
print(timeit.repeat(light, repeat=5, number=1000))
