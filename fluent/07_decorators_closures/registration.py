registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry) # registry contains f1 and f2 here already
    f1()
    f2()
    f3()
    print('registry ->', registry)


if __name__ == '__main__':
    main()
