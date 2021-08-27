from collections import defaultdict

visits = {'Mexico': {'Tulum', 'Puerto Vallarta'}, 'Japan': {'Hakone'}}
visits.setdefault('France', set()).add('Arles') # short
if (japan := visits.get('Japan')) is None:      # long
    visits['Japan'] = japan = set()
japan.add('Kyoto')

print(visits)


class VisitsBad:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = VisitsBad()
visits.add('Russia', 'Yekatarinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add('England', 'Dover')
visits.add('England', 'Avery')
print(visits.data)


pictures = {}
path = 'profile_1234.png'

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()
print(image_data)


def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
