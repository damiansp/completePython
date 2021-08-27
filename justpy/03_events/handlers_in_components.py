import justpy as jp


class ButtonDiv(jp.Div):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 6):
            b = jp.Button(text=f'Button {i}',
                          a=self,
                          classes='m-2 p-2 border text-blue text-lg')
            b.n = i
            b.on('click', self.button_click)
        self.info_div = jp.Div(
            text='info here', a=self, classes='m-2 p-2 border')

    def button_click(self, msg):
        print(self)
        print(msg.target)
        self.info_div.text = f'Button {msg.target.n} clicked'


def test():
    wp = jp.WebPage()
    ButtonDiv(a=wp)
    return wp


jp.justpy(test)
