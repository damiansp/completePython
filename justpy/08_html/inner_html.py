import justpy as jp

P = 'm-2 p-2 text-xl'
DIV = 'm-4 p-4 text-3xl'


my_html = f'''
<div>
  <p class="{P} text-red-500">Paragraph 1</p>
  <p class="{P} text-blue-500">Paragraph 2</p>
  <p class="{P} text-green-500">Paragraph 3</p>
</div>'''


def demo():
    wp = jp.WebPage()
    d = jp.Div(a=wp, classes=DIV)
    d.inner_html = '<pre>Hello, there.\n How goes it?</pre>'
    jp.Div(a=wp, inner_html=my_html)
    for color in ['red', 'green', 'blue', 'pink', 'yellow', 'teal', 'purple']:
        jp.Div(
            a=wp,
            inner_html=f'<p class="ml-2 text-{color}-500 text-3xl">{color}</p>')
    return wp


jp.justpy(demo)
