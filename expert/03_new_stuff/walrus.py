import os
import re
import sys


import_re = re.compile(r'^\s*import\s+\.{0,2}((\w+\.)*(\w+))\s*$')
import_from_re = re.compile(
    '^\s*from\s+\.{0,2}((\w+\.)*(\w+))\s+import\s+(\w+|\*)+\s*$')


def print_matches(filename):
    with open(filename) as f:
        for line in f:
            match = import_re.search(line)
            if match:
                print(match.groups()[0])
            match = import_from_re.search(line)
            if match:
                print(match.groups()[0])

                
def better_print_matches(filename):
    with open(sys.argv[1]) as f:
        for line in f:
            if match := import_re.match(line):
                print(match.groups()[0])
            if match := import_from_re.match(line):
                print(match.groups()[0])


#name = 'Bob'
#surname = 'Dobolina'
#height = 185
#weight = 72
#user = {'name': name,
#        'surname': surname,
#        'display_name': f'{name} {surname.upper()}',
#        'height': height,
#        'weight': weight,
#        'bmi': weight / (height / 2) ** 2}

better_user = {'name': (name := 'Bob'),
               'surname': (surname := 'Dobolina'),
               'display_name': f'{name} {surname.upper()}',
               'height': (height := 185),
               'weight': (weight := 72),
               'bmi': weight / (height / 2) ** 2}
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'usage: {os.path.basename(__file__)} filename')
        sys.exit(1)
    print_matches(sys.argv[1])
    better_print_matches(sys.argv[1])
