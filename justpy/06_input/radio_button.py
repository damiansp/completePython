import justpy as jp


LABEL = 'inline-block mb-1 p-1'

def radio():
    wp = jp.WebPage()
    genders = ['male', 'female', 'both', 'other']
    ages = [(0, 30), (31, 60), (61, 90), (91, 120)]
    outer_div = jp.Div(classes='border m-2 p-4 w-64', a=wp)
    jp.P(a=outer_div, text='Select your gender:')
    for gender in genders:
        label = jp.Label(classes=LABEL, a=outer_div)
        radio_btn = jp.Input(
            type='radio', name='gender', value=gender, a=label)
        jp.Span(classes='ml-1', a=label, text=gender.capitalize())
    jp.Div(a=outer_div, classes='m-2')
    jp.P(a=outer_div, text='Age:')
    for age in ages:
        label = jp.Label(classes=LABEL, a=outer_div)
        radio_btn = jp.Input(type='radio', name='age', value=age[0], a=label)
        jp.Span(classes='ml-1', a=label, text=f'{age[0]} - {age[1]}')
        jp.Br(a=outer_div)
    return wp


jp.justpy(radio)
