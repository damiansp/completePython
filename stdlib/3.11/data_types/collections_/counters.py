from collections import Counter
import re


cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

#words = re.findall(r'\w+', open('hamlet.txt').read().lower())
#Counter(words).most_commone(10)

# initializing
c = Counter()
c = Counter('gallahad')
c = Counter({'red': 5, 'blue': 2})
c = Counter(cats=4, dogs=8)
c = Counter(['eggs', 'ham'])
print(c['bacon'])  # 0
print(c)

c['bacon'] = 0
print(c)
del c['bacon']


c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))

print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c - d)  # {'a': 3}
c.subtract(d)
print(c)      # {'a': 3, 'b': 0, 'c': -3, 'd': -6}

print(d.total())  # 10

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)  # {'a': 4, 'b': 3}
print(c - d)  # {'a': 2}
print(c & d)  # {'a': 1, 'b': 1}
print(c | d)  # {'a': 3, 'b': 2}
print(c == d)  # False
print(c <= d)  # False

c = Counter(a=2, b=-4)
print(+c)  # {'a': 2}
print(-c)  # {'b': 4}
