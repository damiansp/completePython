from math import sqrt
import _thread as thread


def main():
    data = [2, 193, 323, 1327, 433785905, 433785907, 433785909, 433785911]
    for x in data:
        thread.start_new_thread(is_prime, (x,))
    # don't allow program to terminate before threads complete:
    a = input('Type something to quit:\n')

        
def is_prime(x):
    if x < 2:
        print(f'{x} is not prime')
        return
    if x == 2:
        print(f'{x} is prime')
        return
    if x % 2 == 0:
        print(f'{x} is not prime')
        return
    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            print(f'{x} is not prime')
            return
    print(f'{x} is prime')


if __name__ == '__main__':
    main()
