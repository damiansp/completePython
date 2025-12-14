import re


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

for i in range(4):
    print(m.group(i))  # 11/27/12, 11, 27, 2012
print(m.groups)  # <built-in method groups of re.Match object at ...>
month, day, year = m.groups()

text = 'today is 12/14/2025, Chirstmas in on 12/25/2025.'
for m, d, y in datepat.findall(text):
    print(f'{y}-{m}-{d}')  # 2025-12-14, 2025-12-25

for m in datepat.finditer(text):
    print(m.groups())  # ('12', '14', '2025'), ('12', '25', '2025')
