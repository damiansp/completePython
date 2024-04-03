def main():
    for f in [100, 75, 50, 25]:
        print(f'{f}F = {f2c(f):.2f}C')
              

class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return (
            f'Farhenheit value must be on range [{self.min_f}, {self.max_f}], '
            f'got {self.f}')


def f2c(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32) * 5/9


if __name__ == '__main__':
    main()
    
