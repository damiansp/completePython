a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = {'three': 3, 'one': 1, 'two': 2}
print(a == b == c == d) # True
         
