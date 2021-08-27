import justpy as jp


P = 'text-2xl m-2 m-1 text-red-500'


def demo():
    wp = jp.WebPage()
    jp.Div(text='This text not shown', a=wp)
    wp.html = f'<p class="{P}">Hello, World!</p>'
    jp.Div(text='Also not shown', a=wp)
    return wp


jp.justpy(demo)
