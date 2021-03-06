import justpy as jp


def color_demo(req):
    wp = jp.WebPage()
    in1 = jp.Input(type='color',
                   a=wp,
                   classes='m-2 p-2',
                   style='width: 100px; height: 100px',
                   input=color_change,
                   debounce=30)
    in1.d = jp.Div(text='Click box above to change my color',
                   a=wp,
                   classes='border m-2 p-2 text-2xl font-bold')
    return wp


def color_change(self, msg):
    self.d.style = f'color: {self.value}'
    self.d.text = f'The color of this text is {self.value}'


jp.justpy(color_demo)
