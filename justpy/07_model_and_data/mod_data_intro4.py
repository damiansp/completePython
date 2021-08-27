import justpy as jp


BUTTON = ('w-32 m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 '
          'px-4 rounded')
DIV = 'm-2 p-2 h-32 text-xl border-2 overflow-auto'
INPUT = ('m-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded '
         'xtw-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white '
         'focus:border-purple-500')


async def input_demo(req):
    wp = jp.WebPage(data={'text': 'Init text'})
    b = jp.Button(text='Reset', click=reset_all, a=wp, classes=BUTTON)
    jp.Hr(a=wp)
    for _ in range(5):
        jp.Input(
            a=wp, classes=INPUT, placeholder='Type away!', model=[wp, 'text'])
    for _ in range(3):
        jp.Div(model=[wp, 'text'], classes=DIV, a=wp)
    return wp


def reset_all(self, msg):
    msg.page.data['text'] = ''


jp.justpy(input_demo)
