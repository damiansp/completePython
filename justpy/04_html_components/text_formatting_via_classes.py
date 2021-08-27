import justpy as jp


def html_comps():
    wp = jp.WebPage()
    jp.Div(text='Italicize me', a=wp, classes='italic')
    jp.Div(text='Embolden me', a=wp, classes='font-bold')
    return wp


jp.justpy(html_comps)
