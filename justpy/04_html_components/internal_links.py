import justpy as jp


def link_demo():
    wp = jp.WebPage()
    link = jp.A(
        text='Scroll to target',
        a=wp,
        classes=('inline-block m-2 p-2 text-xl text-white bg-blue-500 '
                 'hover:bg-blue-700'))
    for i in range(50):
        jp.P(text=f'{i + 1} Not the target',
             classes='m-1 p-1 text-white bg-blue-300',
             a=wp)
    target = jp.A(text='Stay on target!',
                  classes='inline-block m-1 p-1 text-white bg-red-500',
                  a=wp)
    link.bookmark = target
    link.scroll = True
    target.bookmark = link
    for i in range(50):
        jp.P(text=f'{i + 51} Not the target',
             classes='m-1 p-1 text-white bg-blue-300',
             a=wp)
    return wp


jp.justpy(link_demo)
