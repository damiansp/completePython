def main():
    arg = 4
    square(arg)
    print(arg) # 4


def square(x):
    x *= x
    print(f'In square: x={x}')


main()

