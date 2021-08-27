import pandas as pd


s = pd.Series(list('abbccc')).astype('category')
print(s)
print(s.cat.categories)

s = s.cat.rename_categories(list('cba'))
s = s.cat.reorder_categories(list('cba'))
print()
print(s)
print(s.cat.categories)

s = s.cat.add_categories(['d', 'e'])
s = s.cat.remove_categories(['b'])
print()
print(s)
print(s.cat.categories)

s = s.cat.remove_unused_categories()
print()
print(s)
print(s.cat.categories)

s = s.cat.set_categories(list('abcde'))
s = s.cat.as_ordered() 
print()
print(s)
print(s.cat.categories)

s = s.cat.as_unordered()
print()
print(s)
print(s.cat.categories)
