fresh_fruit = {'apple': 10, 'banana': 8, 'lemon': 5}


def make_lemonade(n):
    print(f'Made {n} lemonade{"s" if n != 1 else ""}')


def out_of_stock():
    print('Out of stock')


count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# Better:
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()


def make_cider(n):
    print(f'Made {n} cider{"s" if n != 1 else ""}')


if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

    
