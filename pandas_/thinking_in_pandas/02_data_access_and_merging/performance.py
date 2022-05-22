import pandas as pd


restaurant_inspections = pd.DataFrame({
    'restaurant': ['Diner', 'Diner', 'Pandas', 'Pandas'],
    'location': [(4, 2), (4, 2), (5, 4), (5, 4)],
    'date': ['2022-02-18', '2022-05-18', '2022-04-18', '2022-01-18'],
    'score': [90, 100, 55, 60]})
print(restaurant_inspections)

# Better representation w multi-index
restaurants = pd.MultiIndex.from_tuples(
    (
        ('Diner', (4, 2)),
        ('Diner', (4, 2)),
        ('Pandas', (5, 4)),
        ('Pandas', (5, 4))),
    names=['restaurant', 'location'])
inspections = pd.DataFrame(
    {'date': ['2022-02-18', '2022-05-18', '2022-04-18', '2022-01-18'],
     'score': [90, 100, 55, 76]},
    index=restaurants)
print(inspections)

# Multi-index cols
rests = pd.MultiIndex.from_tuples(
    (('Diner', (4, 2)), ('Pandas', (5, 4))), names=['restaurant', 'location'])
inspex = pd.MultiIndex.from_tuples(
    ((1, 'score'), (1, 'date'), (2, 'score'), (2, 'date')),
    names=['inspection', None])
insp = pd.DataFrame(
    [[90, '02/19', 100, '05/18'], [55, '04/18', 76, '01/18']],
    index=rests,
    columns=inspex)
print(insp)


total_inspections = restaurant_inspections.groupby(
    ['restaurant', 'location'], as_index=False
)['score'].count()
total_inspections.rename(columns={'score': 'total'}, inplace=True)
print(total_inspections)

restaurant_inspections = pd.merge(
    restaurant_inspections, total_inspections, how='outer')
print(restaurant_inspections)


