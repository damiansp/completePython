import sys

VERSION = sys.version.split()[0]


s = 'my lovely little string'

print(s.center(80))
print(s.rjust(80))

l_count = s.count('l')        # 4
l_word_count = s.count(' l')  # 2
print(l_count)
print(l_word_count)

tt_pos = s.find('tt')      # 12
print(tt_pos)
last_t_pos = s.rfind('t')  # 18
print(last_t_pos)
ll_pos = s.find('ll')      # -1
print(ll_pos)


class DefaultFormatMap(dict):
    def __missing__(self, key):
        return f'<{key}>'

    
print('{name} was born in {country}'.format_map(DefaultFormatMap(name='Guido')))

o_idx = s.index('o')  # 4
print(o_idx)
try:
    x_idx = s.index('x')
except ValueError:
    x_idx = -1
print(x_idx)          # -1

parts = s.partition(' ')
print(parts)  # ('my', ' ', 'lovely little string')

if VERSION >= '3.9':
    no_pre = s.removeprefix('my lovely ')
    print(no_pre)
else:
    print('str.removeprefix() unavailable')

text = (
    'ab c\n'
    '\n'
    'de fg\r'
    'kl\r'
    '\n')
print(text.splitlines())
print(text.splitlines(keepends=True))
