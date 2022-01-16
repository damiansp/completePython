from graphlib import TopologicalSorter


table_refs = {'customers': set(),
              'accounts': {'customers'},
              'products': set(),
              'orders': {'accounts', 'customers'},
              'order_products': {'orders', 'products'}}
sorter = TopologicalSorter(table_refs)
print(list(sorter.static_order()))
