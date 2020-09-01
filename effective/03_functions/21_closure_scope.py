def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 7}
sort_priority(numbers, group)
print(numbers) # 2 3 7 1 4 5 6 8


def sort_priority2(values, group):
    found = False         # Scoe: sort_priority2
    def helper(x):
        if x in group:
            found = True # Scope: helper (not what we want...)
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found) # False! not as desired...
print(numbers)


def sort_priority3(values, group):
    found = False
    def helper(x):
        nonlocal found # refers to prev
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority3(numbers, group)
print('Found:', found) # True
print(numbers)


# But like globals, non-locals can have unexpected, hard to debug side effects
# and are best avoided...
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
print('Found:', sorter.found) # True
            
