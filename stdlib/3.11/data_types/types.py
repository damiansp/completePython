from types import GenericAlias


print(list[int] == GenericAlias(list, (int,)))           # True
print(dict[str, int] == GenericAlias(dict, (str, int)))  # True
