def example(a, b, **kw):
    return a * b

print(type(example))
print(example.__code__.co_varnames, example.__code__.co_argcount)

mersenne = lambda x: 2**x - 1
print(type(mersenne))
print(mersenne(17))


# Higher-order Functions
year_cheese = [
    (2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),(2004, 31.33),
    (2005, 32.62), (2006, 32.73), (2007, 33.5), (2008, 32.84), (2009, 33.02),
    (2010, 32.92)]
print(max(year_cheese))
print(max(year_cheese, key=lambda yc: yc[1]))

