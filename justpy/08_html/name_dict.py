import justpy as jp


P = 'm-2 p-2 text-%s-500 text-xl'


async def demo(req):
    wp = jp.WebPage()
    c = jp.parse_html(
        f'''
        <div>
          <p class="{P}">Paragraph 1</p>
          <p class="{P}" name="p2">Paragraph 2</p>
          <p class="{P}">Paragraph 3</p>
        </div>''' % ('red', 'blue', 'green'),
        a=wp)
    p2 = c.name_dict['p2']
    p2.on('click', click_me)
    return wp
    

def click_me(self, msg):
    self.text = 'I am clicked'


jp.justpy(demo)
