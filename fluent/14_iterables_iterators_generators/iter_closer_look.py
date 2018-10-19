from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print(d6_iter) # callable iterator

for roll in d6_iter:
    print(roll)
