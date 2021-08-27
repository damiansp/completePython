import justpy as jp


INPUT = ('m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 '
         'text-gray-700 focus:outline-none focus:bg-white '
         'focus:border-purple-500')
P = 'm-2 p-2 h-32 text-xl border-2'


async def my_input(self, msg):
    self.div.text = self.value


async def input_demo(req):
    wp = jp.WebPage()
    in1 = jp.Input(
        a=wp, classes=INPUT, placeholder='Enter text', input=my_input)
    in1.div = jp.Div(text='Your stuff here', classes=P, a=wp)
    #in1.on('input', my_input)
    return wp


jp.justpy(input_demo)
