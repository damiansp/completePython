import collections


Event = collections.namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):
    '''Yield to simulator issuing event at each state change'''
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')


taxi = taxi_process(ident=54, trips=2)
print(next(taxi))
taxi.send(_.time + 7)
taxi.send(_.time + 23)
taxi.send(_.time + 5)
taxi.send(_.time + 48)
taxi.send(_.time + 1)
taxi.send(_.time + 10)
