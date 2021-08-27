import justpy as jp


P = 'm-2 p-2 text-%s-500 text-xl'


def demo():
    wp = jp.WebPage()
    root = jp.Div(a=wp)
    c1 = jp.Div(a=root)
    c2 = jp.P(classes=P % 'red', a=c1, text='Paragraph 1')
    c3 = jp.P(classes=P % 'blue', a=c1, text='Paragraph 2')
    c4 = jp.P(classes=P % 'green', a=c1, text='Paragraph 3')
    return wp

jp.justpy(demo)
