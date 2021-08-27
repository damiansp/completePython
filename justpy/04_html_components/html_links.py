import justpy as jp


def link_demo():
    wp = jp.WebPage()
    jp.A(text='Python Org',
         href='https://python.org',
         a=wp,
         classes='m-2 p-2 text-xl text-white bg-blue-500 hover:bg-blue-700')
    return wp


jp.justpy(link_demo)
