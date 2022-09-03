import cProfile
import pstats
import time
import tempfile


def profile(column='time', list=3):
    def parameterized_decorator(f):
        def decorated(*args, **kwargs):
            s = tempfile.mktemp()
            profiler = cProfile.Profile()
            profiler.runcall(f, *args, **kwargs)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            print('=' * 5, f'{f.__name__}() profile', '=' * 5)
            p.sort_stats(column).print_stats(list)
        return decorated
    return parameterized_decorator


def medium():
    time.sleep(0.01)


@profile('time')
def heavy():
    for _ in range(100):
        medium()
        medium()
    time.sleep(2)


def main():
    for _ in range(2):
        heavy()


if __name__ == '__main__':
    main()
