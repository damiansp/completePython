import justpy as jp


DIV = 'm-2 p-2 border'
GREENSPAN = 'text-green-500 mr-6'
REDSPAN = 'text-red-500 mr-6'
LABEL = 'inline-block mb-1 p-1'


def radio_changed(self, msg):
    self.result_div.text = ''
    d = jp.Div(a=self.result_div, classes=DIV)
    for btn in self.btn_list:
        if btn.checked:
            jp.Span(text=f'{btn.value} is checked', a=d, classes=GREENSPAN)
        else:
            jp.Span(test=f'{btn.value} not checked', a=d, classes=REDSPAN)


def radio_test():
    wp = jp.WebPage()
    genders = ['male', 'female', 'other']
    ages = [(0, 30), (31, 60), (61, 90)]
    outer_div = jp.Div(classes=DIV + 'w-64', a=wp)
    result_div = jp.Div(text='Click buttons to see results here:',
                        classes='m-2 p-2 text-xl')

    jp.P(a=outer_div, text='Select gender:')
    gender_list = []
    for gender in genders:
        label = jp.Label(classes=LABEL, a=outer_div)
        radio_btn = jp.Input(type='radio',
                             name='gender',
                             value=gender,
                             a=label,
                             btn_list=gender_list,
                             result_div=result_div,
                             change=radio_changed)
        gender_list.append(radio_btn)
        jp.Span(classes='ml-1', a=label, text=gender.capitalize())

    jp.Div(a=outer_div, classes='m-2')

    jp.P(a=outer_div, text='Select age:')
    age_list = []
    for age in ages:
        label = jp.Label(classes=LABEL, a=outer_div)
        radio_btn = jp.Input(type='radio',
                             name='age',
                             value=age[0],
                             a=label,
                             btn_list=age_list,
                             result_div=result_div,
                             change=radio_changed)
        age_list.append(radio_btn)
        jp.Span(classes='m1-l', a=label, text=f'{age[0]} - {age[1]}')
        jp.Br(a=outer_div)
    wp.add(result_div)
    return wp


jp.justpy(radio_test)
