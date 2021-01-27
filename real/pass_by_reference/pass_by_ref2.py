def main():
    n = 9001
    print(f'Init: address of n: {id(n)}') # addA
    incr(n)
    print(f'End: address of n: {id(n)}')  # addA


def incr(x):
    print(f'Init: address of x: {id(x)}') # addA
    x += 1
    print(f'End: address of x: {id(x)}')  # addB


main()
