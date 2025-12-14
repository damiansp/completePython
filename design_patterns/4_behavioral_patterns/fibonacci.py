def main():
    fib = Fibonacci(100)
    for n in fib:
        print(n)


class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        res = self.current
        self.current, self.previous = (
            self.current + self.previous, self.current)
        return res


if __name__ == '__main__':
    main()
