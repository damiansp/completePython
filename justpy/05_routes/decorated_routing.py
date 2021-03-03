import justpy as jp


P_CLASSES = 'text-5xl m-2'


@jp.SetRoute('/hello')
def hello():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello, World!', classes=P_CLASSES))
    return wp


@jp.SetRoute('/bye')
def bye():
    wp = jp.WebPage()
    wp.add(jp.P(text='Goodbye!', classes=P_CLASSES))
    return wp


jp.justpy()
