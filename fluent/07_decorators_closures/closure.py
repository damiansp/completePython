class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_val):
        self.series.append(new_val)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(1))
print(avg(1))
print(avg(2))
print(avg(3))
print(avg(5))
print(avg(8))
print(avg(13))
print(avg(25))


def make_averager():
    series = []

    def averager(new_val):
        series.append(new_val)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()
print(avg(1))
print(avg(1))
print(avg(2))
print(avg(3))
print(avg(5))
print(avg(8))
print(avg(13))
print(avg(25))

