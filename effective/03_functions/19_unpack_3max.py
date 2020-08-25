def get_stats(x):
    minimum = min(x)
    maximum = max(x)
    return minimum, maximum

lengths = [64, 73, 74, 60, 58, 55, 71, 62, 71, 70]
mn, mx = get_stats(lengths)
print(f'Min: {mn}; Max: {mx}')


def get_avg_ratio(x):
    avg = sum(x) / len(x)
    scaled = [i / avg for i in x]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest:  {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')


# Assume at some future time, needs to return mean, median, and n as well...
def get_stats2(x):
    minimum = min(x)
    maximum = max(x)
    n = len(x)
    mean = sum(x) / n
    sorted_x = sorted(x)
    middle = n // 2
    if n % 2 == 0:
        lower = sorted_x[middle - 1]
        upper = sorted_x[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_x[middle]
    return minimum, maximum, mean, median, n

mn, mx, mean, med, n = get_stats2(lengths)
print(f'Min: {mn}\nMx: {mx}\nMean: {mean}\nMed: {med}\nN: {n}')


# Problems:
# - easy to swap values accidentally
# - long unpacking statements make for unsightly hard-to-read code
# - prefer returning a dict, named tuple, or small class
