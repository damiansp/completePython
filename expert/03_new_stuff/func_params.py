def concatenate(first: str, second: str, delim: str):
    return delim.join([first, second])


# Before / are positional only, after * are kwargs only
def concat(first: str, second: str, /, *, delim: str):
    return delim.join([first, second])

#concat('Bob', 'Dobolina', ' ') # 3rd arg must be kw


def conc(*items, delim: str):
    return delim.join(items)

print(conc('Bob', 'Dobolina', delim=' '))
print(conc('Ronald', 'Reuel', 'Tolkien', delim=' '))
print(conc('Jay', delim='-')) # 'Jay'
print(conc(delim='!'))        # ''


