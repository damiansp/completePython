import functools


class SnareDrum:
    pass


class Cymbal:
    pass


class Stick:
    pass


class Brush:
    pass


@functools.singledispatch
def play(instrument, accessory):
    raise NotImplementedError('Play not defined')


@play.register(SnareDrum)
def _(instrument, accessory):
    if isinstance(accessory, Stick):
        return 'Pok!'
    if isinstance(accessory, Brush):
        return 'Shhhhht'
    raise NotImplementedError('Play not defined')


@play.register(Cymbal)
def _(instrument, accessory):
    if isinstance(accessory, Brush):
        return 'Frishhhhhht'
    raise NotImplementedError('Play not defined')


print(play(SnareDrum(), Stick()))
print(play(SnareDrum(), Brush()))
print(play(Cymbal(), Brush()))
