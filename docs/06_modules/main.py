import fibo

fibo.fib(8)
res = fibo.fib2(10000)
print(res)


if __name__ == '__main__':
    # Run as > python3 main.py [n]
    import sys
    fibo.fib(int(sys.argv[1]))
