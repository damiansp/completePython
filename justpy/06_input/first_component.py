import justpy as jp


def input_demo(req):
    wp = jp.WebPage()
    for _ in range(10):
        InputWithDiv(a=wp)
    return wp


class InputWithDiv(jp.Div):
    input_classes = (
        'm-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 '
        'text-gray-700 focus:outline-none focus:bg-white '
        'focus:border-purple-500')
    out_div = 'm-2 p-2 h-32 text-xl border-2'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in1 = jp.Input(a=self,
                            classes=self.input_classes,
                            placholder='Typez vous',
                            input=self.input_handler)
        self.in1.div = jp.Div(
            text='What you typed:', classes=self.out_div, a=self)
        
    @staticmethod
    def input_handler(self, msg):
        self.div.text = self.value


jp.justpy(input_demo)
    
