# 3. Manual formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926'.zfill(5))
