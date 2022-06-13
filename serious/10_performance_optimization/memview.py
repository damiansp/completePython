s = b'abcdefgh'
view = memoryview(s)  # memoryview is a pointer/ref, not a copy
print(view[1])        # 98 (b)
lim = view[1:3]
print(lim)            # <memory at...>
print(bytes(lim))     # b'bc'
