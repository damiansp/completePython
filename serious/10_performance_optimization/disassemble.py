import dis


def meaning():
    return 42

def howdy(pardner):
    print(f'Howdy, {pardner}')
    

print(dis.dis(meaning))
print(dis.dis(howdy))


abc = ('a', 'b', 'c')


def concat1():
    for c in abc:
        abc[0] + c

def concat2():
    a = abc[0]
    for c in abc:
        a + c


print(dis.dis(concat1))
print(dis.dis(concat2))


def deep_meaning():
    
    def meaning():
        return 42

    return meaning()


print(dis.dis(deep_meaning))


def deep2():
    secret = 42
    def meaning():
        retru secret

    return meaning()


print(dis.dis(deep2))
