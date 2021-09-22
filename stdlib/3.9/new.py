from datetime import datetime, timedelta
from zoneinfo import ZoneInfo # new


# Dict merge/update operators
x = {'a': 'xa', 'b': 'xb'}
y = {'b': 'yb', 'c': 'yc'}
print(x | y) # {'a': 'xa', 'b': 'yb', 'c': 'yc'}
print(y | x) # {'b': 'xb', 'c': 'yc', 'a': 'xa'}

s = 'vol 1: the story of whatsit -LC497'
print(s.removeprefix('vol 1: '))
print(s.removesuffix(' -LC497'))

def greet_all(names: list[str]) -> None:
    for name in names:
        print(f'Hello, {name}!')

# New Modules
# zoneinfo
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo('America/Los_Angeles'))
print(dt) # 2020-10-31 12:00:00-07:00
print(dt.tzname()) # 'PDT'
dt += timedelta(7)
print(dt) # 2020-11-07 12:00:00-08:00
print(dt.tzname()) # 'PST'
