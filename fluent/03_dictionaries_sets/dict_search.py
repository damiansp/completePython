class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key
    
    
d = StrKeyDict0([('2', 'two'), ('4', 'four')])

for k in ['2', 4, 1]:
    print('Key: ', k)
    try:
        print('d[k]:')
        print(d[k])
    except Exception as e:
        print(e)

    try:
        print('d.get(k):')
        print(d.get(k))
    except Exception as e:
        print(e)

    try:
        print('k in d:')
        print(k in d)
    except Exception as e:
        print(e)


