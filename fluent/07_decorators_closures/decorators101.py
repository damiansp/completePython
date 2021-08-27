'''
@decorate
def target():
    print('running target()')

# Equivalent to:
def target():
    print('running target()')

target = decorate(target)
'''

def deco(func):
    def inner():
        print('running inner()')
        func()
    return inner

@deco
def target():
    print('running target()')

print(target)   # <function deco.<locals>.inner at 0x...>
print(target()) # running inner() running target()
