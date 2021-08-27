import locale
import pyuca

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits)) # ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(sorted(fruits, key=locale.strxfrm)) # doesn't work on OSX

coll = pyuca.Collator()
print(sorted(fruits, key=coll.sort_key))
