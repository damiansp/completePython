
# Strictly procedural:
s = 0
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n
print(s)


# OOP
m = list()
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)
print(sum(m))


class SummableList(list):
    def sum(self):
        s = 0
        for v in self.__iter__():
            s += v
        return s

    
# Functional
def sum(seq):
    if len(seq) == 0: return 0
    return seq[0] + sum(seq[1:])

def until(n, filter_func, v):
    if v == n: return []
    if filter_func(v): return [v] + until(n, filter_func, v + 1)
    else: return until(n, filter_func, v + 1)

mult_3_5 = lambda x: x % 3 == 0 or x % 5 == 0

# Tests
print(mult_3_5(3)) # True
print(mult_3_5(4)) # False
print(mult_3_5(5)) # True

print(until(10, mult_3_5, 0)) # [0, 3, 5, 6, 9]


