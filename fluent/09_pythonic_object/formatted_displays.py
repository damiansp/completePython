from datetime import datetime

brl = 1 / 2.43 # BRL -> USD conversion rate
print(brl)

print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print(format(42, 'b'))
print(format(2/3, '.1%'))


now = datetime.now()
print(format(now, '%H:%M:%S'))
print('It is now {:%I:%M %p}'.format(now))
