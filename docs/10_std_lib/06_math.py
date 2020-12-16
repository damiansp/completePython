import math
import random
import statistics as stats


print(math.cos(math.pi / 4))
print(math.log(1000000, 2))

print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample(range(100), 10)) # w/o replacement
print(random.random()) # float on (0, 1)
print(random.randrange(6)) # rand int from range(6) [0, 6) = [0, 5]

x = [1.23, 4.56, 7.89, 0.12, 3.45, 6.78]
print(stats.mean(x))
print(stats.median(x))
print(stats.variance(x))
