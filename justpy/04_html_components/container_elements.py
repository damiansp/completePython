import justpy as jp


def html_comps():
    wp = jp.WebPage()
    for i in range(10):
        d = jp.Div(a=wp, classes='m-2')
        for j in range(5):
            jp.Span(text=f'Div {i + 1:02d} - Span {j + 1:02d}',
                    a=d,
                    classes='text-white bg-blue-700 hover:bg-blue-200 ml-1 p-1')
    return wp


jp.justpy(html_comps)
