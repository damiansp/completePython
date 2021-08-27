stock = {'nails': 125, 'screws': 35, 'wingnuts': 8, 'washers': 24}
order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size

BATCH_SIZE = 8

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, BATCH_SIZE)
    if batches:
        result[name] = batches

print(result) # screws: 4, wingnuts: 1


# More succinctly:
res = {name: get_batches(stock.get(name, 0), BATCH_SIZE)
       for name in order if get_batches(stock.get(name, 0), 8)}
print(res) # same

# ...but unnecessary duplicate computation


res = {name: batches for name in order
       if (batches := get_batches(stock.get(name, 0), BATCH_SIZE))}
print(res) # et voila


# Syntactical issues
#res = {name: (tenth := count // 10) for name, count in stock.items()
#       if tenth > 0}
# NameError: tenth is not defined

res = {name: tenth for name, count in stock.items()
       if (tenth := count // 10) > 0}
print(res) # nails: 12, screws: 3, washers: 2


# Loop leak:
half = [(last := count // 2) for count in stock.values()]
print(f'Last item of {half} is {last}') # last still in scope!

# cf: 
for count in stock.values(): # leaky
    pass
print(f'Last item of {list(stock.values())} is {count}') # count in scope too

# Best to avoid leaking variables... clutters namespace and wastes memory


# With generators:
found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), BATCH_SIZE)))
print(next(found)) # screws, 4
print(next(found)) # wingnuts, 1
