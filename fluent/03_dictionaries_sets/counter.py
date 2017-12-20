from collections import Counter

ct = Counter('abracadabra')
print(ct)

ct.update('damiansatterthwaitephillips')
print(ct)
print(ct.most_common(3))
