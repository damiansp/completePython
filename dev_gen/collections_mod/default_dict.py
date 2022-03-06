from collections import defaultdict


d = defaultdict(int)
a = [1, 2, 3, 4, 2, 4, 1, 2]
for i in a:
    d[i] += 1  # already set to 0 by default
print(d)


ld = defaultdict(list)
for i in range(5):
    ld[i] += [i, 2*i]
print(ld)
