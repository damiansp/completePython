import justpy as jp


def html_comps():
    wp = jp.WebPage()
    jp.get_tag('i', text='italic text', a=wp)
    for _ in range(4):
        jp.get_tag('br', a=wp)
    jp.get_tag('strong', text='big strong text', a=wp)
    return wp


jp.justpy(html_comps)
