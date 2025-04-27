from collections import defaultdict
from itertools import groupby
from operator import itemgetter


rows = [
    {'address': '5412 N Clark', 'date': '2012-07-01'},
    {'address': '5148 N Clark', 'date': '2012-07-04'},
    {'address': '5800 E 58th', 'date': '2012-07-02'},
    {'address': '2122 N Clark', 'date': '2012-07-02'},
    {'address': '5645 N Ravenswood', 'date': '2012-07-03'},
    {'address': '1060 W Addison', 'date': '2012-07-02'},
    {'address': '4801 N Broadway', 'date': '2012-07-01'},
    {'address': '1039 W Granville', 'date': '2012-07-04'}]
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for r in rows_by_date['2012-07-01']:
    print(r)
