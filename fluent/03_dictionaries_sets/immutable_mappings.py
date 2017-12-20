from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

print('d_proxy:', d_proxy)

try:
    d_proxy[2] = 'x' # fails--proxy is immutable
except TypeError as e:
    print(e)

d[2] = 'B'
print('d:', d)
print('d_proxy:', d_proxy)
