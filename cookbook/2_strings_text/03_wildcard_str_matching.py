from fnmatch import fnmatch, fnmatchcase


print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([n for n in names if fnmatch(n, 'Dat*.csv')])
print(fnmatch('foo.txt', '*.TXT'))  # False on OSX, Unix, True on Windows

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE ST',
    '2122 N CLARK ST',
    '4802 N BROADWAY']
print([a for a in addresses if fnmatchcase(a, '* ST')])
print([a for a in addresses if fnmatchcase(a, '54[0-9][0-9] *CLARK*')])
