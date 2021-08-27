import model5 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# Test
coconuts = LineItem('Brazilian coconut', 20, 17.95)
raisins = LineItem('Sun-dried raising', 5, 4.47)
print(coconuts.weight, coconuts.price) # (20, 17.95)

print(getattr(raisins, '_Quantity#0'), getattr(raisins, '_Quantity#1'))
# (5, 4.47)

print(LineItem.price) # <model5.Quantity object at 0x108b532e8>
