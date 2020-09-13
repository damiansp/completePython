from itertools import islice


def index_words(text):
    res = []
    if text:
        res.append(0)
    for i, letter in enumerate(text):
        if letter == ' ':
            res.append(i + 1)
    return res

address = 'Four score and seven years ago...'
res = index_words(address)
print(res)
for i in res:
    print(address[i], end=' ')
print()


def index_words_iter(text):
    if text:
        yield 0
    for i, letter in enumerate(text):
        if letter == ' ':
            yield i + 1

it = index_words_iter(address)
print(address[next(it)]) # F
print(address[next(it)]) # s


# Lists can also be memory hogs if output list gets arbitrarily long
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('30_generators_or_returned_lists.py', 'r') as f:
    it = index_file(f)
    res = islice(it, 0, 10)
    print(list(res))


# Note though, that generators cannot be reused
