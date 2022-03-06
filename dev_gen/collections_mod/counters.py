from collections import Counter


# init examples
c1 = Counter(['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C'])
c2 = Counter({'A': 3, 'B': 2, 'C': 5})
c3 = Counter(A=4, B=6, C=8)

for c in [c1, c2, c3]:
    print(c)

