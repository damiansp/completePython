from operator import itemgetter


rows = [
    {'name': 'Brian', 'sur': 'Jones', 'id': 1003},
    {'name': 'David', 'sur': 'Beazley', 'id': 1002},
    {'name': 'John', 'sur': 'Cleese', 'id': 1001},
    {'name': 'Eric', 'sur': 'Idle', 'id': 1004},
    {'name': 'James Earl', 'sur': 'Jones', 'id': 1000}]
rows_by_sur = sorted(rows, key=itemgetter('sur'))
rows_by_id = sorted(rows, key=itemgetter('id'))
print(rows_by_sur)
print(rows_by_id)
rows_by_sn = sorted(rows, key=itemgetter('sur', 'name'))
# equivalently:
# rows_by_sn = sorted(rows, key=lambda: r: (r['sur'], r['name']))
print(rows_by_sn)


print(max(rows, key=itemgetter('id')))
