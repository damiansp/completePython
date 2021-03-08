import justpy as jp

BASE = 'm-2 p-2'
CHECKBOX = f'{BASE} form-checkbox'
LABEL = f'{BASE} inline-block'
INPUT = f'{BASE} border block'


def checkbox():
    wp = jp.WebPage(data={'checked': True})
    label = jp.Label(a=wp, classes=LABEL)
    c = jp.Input(
        type='checkbox', classes=CHECKBOX, a=label, model=[wp, 'checked'])
    caption = jp.Span(text='Click to get stuff', a=label)
    in1 = jp.Input(model=[wp, 'checked'], a=wp, classes=INPUT)
    return wp


jp.justpy(checkbox)
