import justpy as jp


P = 'm-2 p-2 text-%s-500 text-xl'
MONO = 'font-mono ml-2'

def demo():
    wp = jp.WebPage()
    c = jp.parse_html(
        f'''
          <div>
            <p class="{P}">Paragraph 1</p>
            <p class="{P}">Paragraph 2</p>
            <p class="{P}">Paragraph 3</p>
          </div>
        ''' % ('red', 'green', 'blue'),
        a=wp)
    for i in c.commands:
        print(i)
        jp.Div(text=i, classes=MONO, a=wp)
    print()
    c = jp.parse_html(
        f'''
          <div>
            <p class="{P}">Paragraph 1</p>
            <p class="{P}">Paragraph 2</p>
            <p class="{P}">Paragraph 3</p>
          </div>
        ''' % ('red', 'green', 'blue'),
        a=wp,
        command_prefix='justpy.')
    for i in c.commands:
        print(i)
        jp.Div(text=i, font=MONO, a=wp)
    return wp


jp.justpy(demo)
