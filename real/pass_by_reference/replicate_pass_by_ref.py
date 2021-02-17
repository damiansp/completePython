def square():
    # Bad choice!
    global n
    n *= n

n = 4
square()
print('n:', n) # 16


def sq(n):
    return n * n

print(sq(4)) # 16
