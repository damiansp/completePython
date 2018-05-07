from datetime import datetime
from stock import Stock
from stock import PriceRule

exchange = {'GOOG': Stock('GOOG'), 'MSFT': Stock('MSFT')}
rule = PriceRule('GOOG', lambda stock: stock.price > 100)

print(rule.matches(exchange))

exchange['GOOG'].update(datetime(2014, 2, 13), 50)
print(rule.matches(exchange))

exchange['GOOG'].update(datetime(2014, 2, 13), 101)
print(rule.matches(exchange))
