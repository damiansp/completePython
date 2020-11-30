def darken(color, scale):
    assert 0 <= scale <= 1, '`scale` must be between 0 and 1'
    color = [comp * scale for comp in color]
    return color


def scale_color(color, scale):
    '''alias for `darken()`'''
    return darken(color, scale)


def saturate(color):
    color = [min(comp, 255) for comp in color]
    return color


def saturate_color(color):
    '''alias for `saturate()`'''
    return saturate(color)


def lerp(v1, v2, factor=0.5, as_int=True):
    '''linear interpolation between `v1` and `v2`'''
    mix = v1 + factor*(v2 - v1)
    if as_int:
        mix = int(round(mix))
    return mix

                
