import asyncio

import justpy as jp


BUTTON = ('m-2 p-2 text-orange-700 bg-white hover:bg-orange-200 '
          'hover:text-orange-500 border focus:border-orange-500 '
          'focus:outline-none')
D = 'text-center m-4 p-4 text-6xl text-red-600 bg-blue-500 faster'
ICON = 'inline-block text-5xl ml-1 mt-1'


def count_test(req):
    start_n = int(req.query_params.get('n', 10))
    animation = req.query_params.get('animation', 'flip')
    wp = jp.WebPage()
    count_button = jp.Button(
        text='Start Countdown', classes=BUTTON, a=wp, click=countdown)
    count_button.start_n = start_n
    count_button.count_animation = animation
    return wp


async def countdown(self, msg):
    self.show = False
    if hasattr(msg.page, 'd'):
        msg.page.remove(msg.page.d)
    bomb_icon = jp.Icon(icon='bomb', classes=ICON, a=msg.page)
    d = jp.Div(classes=D, a=msg.page, animation=self.count_animation)
    msg.page.d = d
    for i in range(self.start_n, 0, -1):
        d.text = str(i)
        await msg.page.update()
        await asyncio.sleep(1)
    d.text = 'Boom!'
    d.animation = 'zoomIn'
    d.set_classes('text-red-500 bg-white')
    bomb_icon.set_class('text-red-700')
    self.show = True
    
    
jp.justpy(count_test)
