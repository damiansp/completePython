import justpy as jp


def html_comps():
    wp = jp.WebPage()
    for j in range(10):
        p = jp.P(
            text='אני אוהב לתכנת בפייתון',
            a=wp,
            contenteditable=True,
            classes='text-white bg-blue-500 hover:bg-blue-700 ml-1 p-1 w-1/2')
        p.dir = 'rtl' # right-to-left
        p.lang = 'he'
    return wp


jp.justpy(html_comps)
