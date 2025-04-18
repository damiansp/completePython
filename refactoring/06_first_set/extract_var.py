def some_func(order):
    return (
        max(0, order.quantity - 500) * order.item_price * 0.05
        + min(order.quntity * order.item_price * 0.1, 100))


# ->
def some_func(order):
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05
    shipping = min(base_price * 0.1, 100)
    return base_price - quantity_discount + shipping

