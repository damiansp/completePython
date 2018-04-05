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
