from typing import Callable


class SortStrategy:
    def __init__(self, f: Callable):
        self.f = f

    def sort(self, data: list):
        return self.f(data)


def bubble_sort(data: list):
    # actal implementation here...
    return sorted(data)


def quick_sort(data: list):
    # actal implementation here...
    return sorted(data, reverse=True)


data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_strat = SortStrategy(bubble_sort)
quick_strat = SortStrategy(quick_sort)
print(bubble_strat.sort(data))
print(quick_strat.sort(data))
