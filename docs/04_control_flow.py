for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else: # executed when no `break` occurs
        # no factor found
        print(n, 'is prime')


def pos_only_arg(arg, /):
    print(arg)


def kw_only_arg(*, arg):
    print(arg)


def combined_args(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)


pos_only_arg(3) # 3
#pos_only_arg(arg=3) # TypeError

#kw_only_arg(5) # TypeError
kw_only_arg(arg=5)


def concat(*args, sep='/'):
    print(sep.join(args))

concat('a', 'b', 'c') # a/b/c
concat('a', 'b', 'c', sep='.') # a.b.c


# Annotations
def f(ham: str, eggs: str='eggs') -> str:
    print('Annotations:', f.__annotations__)
    print('Args:', ham, eggs)
    return ham + ' and ' + eggs

res = f('spam')
print(res)
