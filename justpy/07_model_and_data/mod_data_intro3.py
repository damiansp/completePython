import justpy as jp


INPUT = ('m-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded '
         'xtw-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white '
         'focus:border-purple-500')
DIV = 'm-2 p-2 h-32 text-xl border-2 overflow-auto'


async def input_demo(req):
    wp = jp.WebPage(data={'text': 'Init text'})
    for _ in range(5):
        jp.Input(
            a=wp, classes=INPUT, placeholder='Type away!', model=[wp, 'text'])
    for _ in range(3):
        jp.Div(model=[wp, 'text'], classes=DIV, a=wp)
    return wp


jp.justpy(input_demo)
