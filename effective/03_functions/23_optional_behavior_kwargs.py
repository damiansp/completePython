def remainder(n, divisor):
    return n % divisor

my_kwargs = {'n': 20, 'divisor': 7}
print(remainder(**my_kwargs)) # 6


def print_params(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

print_params(alpha=1, beta=2, gamma='G')
