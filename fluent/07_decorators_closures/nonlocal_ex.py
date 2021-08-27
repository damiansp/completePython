# Broken implementation:
#def make_averager():
#    count = 0
#    total = 0
#
#    def averager(new_val):
#        count += 1               # same as count = count + 1; ref before assign
#        total += new_val
#        return total / count
#
#    return averager

# Fix:
def make_averager():
    count = 0
    total = 0

    def averager(new_val):
        nonlocal count, total
        count += 1
        total += new_val
        return total / count

    return averager

