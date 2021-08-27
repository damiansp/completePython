from datetime import datetime

import justpy as jp


D = 'flex m-2 border'
DIV = 'm-2 h-1/2 border overflow-auto'
BUTTON = ('m-2 p-2 text-orange-700 bg-white hover:bg-orange-200 '
          'hover:text-orange-500 border focus:border-orange-500 '
          'focus:outline-none')
HEADER = (
    'bg-orange-100 border-l-4 border-orange-500 text-orange-700 p-4 text-3xl')
INPUT = ('m-2 bg-gray-200 font-mono appearance-none border-2 border-gray-200 '
         'rounded py-2 px-4 text-gray-700 focus:outline-none focus:bg-white '
         'focus:border-orange-500')
MSG = ('ml-4 p-2 text-lg bg-orange-500 text-white overflow-auto font-mono '
       'rounded-lg')
MSG_ICON = 'text-2xl text-green-600'
OUTER = 'flex flex-col h-screen'
TS = 'text-xs ml-2 flex-shrink-0'


shared_div = jp.Div(clases=DIV, delete_flag=False)
header = jp.Div(text='Simple Message Board', classes=HEADER, delete_flag=False)
button_icon = jp.Icon(icon='paper-plane', classes='text-sm', delete_flag=False)
button_text = jp.Div(text='Send', classes='txt-sm', delete_flag=False)
msg_icon = jp.Icon(icon='comments', classes=MSG_ICON, delete_flag=False)


def msg_demo():
    wp = jp.WebPage()
    outer = jp.Div(classes=OUTER, a=wp)
    outer.add(header)
    d = jp.Div(classes='flex', a=outer)
    msg = jp.Textarea(
        placeholder='Enter message here', a=d, classes=INPUT, debounce=500)
    send_button = jp.Button(a=d, click=send_msg, classes=BUTTON)
    send_button.add(button_icon, button_text)
    outer.add(shared_div)
    shared_div.add_page(wp)
    send_button.message= msg
    return wp


def init_msg():
    # Called once at startup
    d = jp.Div(a=shared_div, classes=D)
    timestamp = jp.P(text=get_timestamp(), classes=TS)
    p = jp.Pre(text='Welcome to the simple message board!', classes=MSG)
    d.add(msg_icon, timestamp, p)


async def send_msg(self, msg):
    print('msg:', msg)
    if self.message.value:
        d = jp.Div(classes=D)
        timestamp = jp.P(text=get_timestamp(), classes=TS)
        p = jp.Pre(text=self.message.value, classes=MSG)
        d.add(msg_icon, timestamp, p)
        shared_div.add_component(d, 0)
        self.message.value = '' # clear msg box after sent
        await shared_div.update()


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

jp.justpy(msg_demo, startup=init_msg)


