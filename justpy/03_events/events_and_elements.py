import justpy as jp


def button_click(self, msg):
    self.n_clicks += 1
    p = jp.P(text=f'{self.text} clicked ({self.n_clicks} times)')
    self.message.add_component(p, 0)
    for button in msg.page.buttons:
        button.set_class('bg-blue-500')
        button.set_class('bg-blue-700', 'hover')
    self.set_class('bg-red-500')
    self.set_class('bg-red-700', 'hover')


def demo():
    n_buttons = 9
    wp = jp.WebPage()
    button_div = jp.Div(classes='flex m-4 flex-wrap', a=wp)
    button_classes = ('w-32 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white '
                      'font-bold py-2 px-4 rounded-full')
    message = jp.Div(classes='text-lg border m-2 p-2 overflow-auto h-64', a=wp)
    message.add(jp.P(text='No clicks'))
    buttons = []
    for i in range(1, n_buttons + 1):
        b = jp.Button(text=f'Button {i}',
                      a=button_div,
                      classes=button_classes,
                      click=button_click)
        b.message = message
        b.n_clicked = 0
        buttons.append(b)
    wp.buttons = buttons
    return wp


jp.justpy(demo)
