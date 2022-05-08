import pandas as pd


bldgs_1844 = pd.DataFrame(
    {'established': [1831, 1842, 1836, 1823]},
    index=pd.MultiIndex.from_tuples(
        [('Grande Hotel', (4, 5)),
         ("Jone's Farm", (1, 2)),
         ('Public Library', (6, 4)),
         ('Marietta House', (1, 7))],
        names=['building', 'location']))
bldgs_2020 = pd.DataFrame(
    {'established': [1962, 1830, 1835, 1924]},
    index=pd.MultiIndex.from_tuples(
        [("Sam's Bakery", (5, 1)),
         ('Grande Hotel', (4, 5)),
         ('Public Library', (6, 4)),
         ('Mayberry Factory', (3, 2))],
        names=['building', 'location']))
# like pd.merge, but implicitly joins on index col(s)
bldgs = bldgs_1844.join(bldgs_2020, how='inner', rsuffix='_2000')
print('bldgs:')
print(bldgs)
