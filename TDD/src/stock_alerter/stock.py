class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError('price cannot be negative')
        self.price_history.append(price)

    @property
    def price(self):
        return self.price_history[-1] if self.price_history else None

    def is_increasing_trend(self):
        last_3 = self.price_history[-3:]
        return last_3[0] < last_3[1] < last_3[2]


    
class PriceRule:
    '''
    PriceRule is a rule that triggers when a stock price satisfies a condition 
    (e.g., greater, equal to, or less than, a given value).
    '''
    def __init__(self, symbol, condition):
        self.symbol = symbol
        self.condition = condition

    def matches(self, exchange):
        try:
            stock = exchange[self.symbol]
        except KeyError:
            return False
        return self.condition(stock) if stock.price else False

    def depends_on(self):
        return {self.symbol}
