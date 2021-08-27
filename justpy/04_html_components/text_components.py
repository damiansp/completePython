import justpy as jp


def html_comps():
    wp = jp.WebPage()
    jp.I(text='Italic text', a=wp)
    jp.Br(a=wp)
    jp.Strong(text='Strong text', a=wp)
    return wp


jp.justpy(html_comps)
