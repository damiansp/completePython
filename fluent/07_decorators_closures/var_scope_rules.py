b = 6

def f2(a):
    print(a)
    print(b)
    b = 9

#f2(3) # throws UnboundLocalError: b referenced before asignment

def f3(a):
    global b
    print(a) # a
    print(b) # 6
    b = 9
    print(b) # 9

f3(3)
print(b)     # 9
