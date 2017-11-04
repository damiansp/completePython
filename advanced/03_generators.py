import sys

# Using a list, build and return the list
def letter_range(a, z):
    res = []
    while ord(a) < ord(z):
        res.append(a)
        a = chr(ord(a) + 1)
    return res

# Same but as a generator function
def letter_range_gen(a, z):
    while ord(a) < ord(z):
        yield a
        a = chr(ord(a) + 1)


def items_in_key_order(d):
    for key in sorted(d):
        yield key, d[key]

        
def items_in_key_order2(d):
    # note: must use tuple() to return a generator
    return ((key, d[key]) for key in sorted(d)) 


def quarters(next_quarter=0.):
    while True: # infinite loop here
        yield next_quarter
        next_quarter += 0.25

res = []
for x in quarters():
    res.append(x)
    if x >= 2.: break # must force termination of inf loop

print(res)


def quarters(next_quarter=0.):
    while True:
        received = (yield next_quarter)

        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received

res = []
generator = quarters()

while len(res) < 10:
    x = next(generator)
    # If x is 0.5, update to 1.
    if abs(x - 0.5) < sys.float_info.epsilon:
        x = generator.send(1.)
    res.append(x)

print(res)


