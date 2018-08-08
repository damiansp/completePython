class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]

f = Foo()
print(f[1])     # 10
for i in f:
    print(i)    # 0, 10, 20

print(20 in f)  # True
print(15 in f)  # False
