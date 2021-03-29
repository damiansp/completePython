import justpy as jp


P = 'm-2 p-2 text-xl text-%s-500'


async def demo(req):
    wp = jp.WebPage()
    c = jp.parse_html(
        f'''
          <div>
            <p class="{P}">Paragraph 1</p>
            <p class="{P}">Paragraph 2</p>
            <p class="{P}">Paragraph 3</p>
          </div>''' % ('red', 'blue', 'green'),
        a=wp)
    print(c)
    print(c.components)
    return wp


jp.justpy(demo)
