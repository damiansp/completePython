import justpy as jp


button_classes = (
    'm-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded')


def show_demo():
    wp = jp.WebPage()
    b = jp.Button(text='Click to toggle show', a=wp, classes=button_classes)
    d = jp.Div(
        text='Toggled by show', classes='m-2 p-2 text-2xl border w-48', a=wp)
    b.d = d
    jp.Div(text='Will always show', classes='m-2', a=wp)
    b.on('click', toggle_show)
    b = jp.Button(
        text='Click to toggle visibility', a=wp, classes=button_classes)
    d = jp.Div(
        text='Toggled by visible', classes='m-2 p-2 text-2xl border w-48', a=wp)
    d.visibility_state = 'visible'
    b.d = d
    jp.Div(text='Will always show', classes='m-2', a=wp)
    b.on('click', toggle_visible)
    return wp


def toggle_show(self, msg):
    self.d.show = not self.d.show


def toggle_visible(self, msg):
    if self.d.visibility_state == 'visible':
        self.d.set_class('invisible')
        self.d.visibility_state = 'invisible'
    else:
        self.d.set_class('visible')
        self.d.visibility_state = 'visible'


jp.justpy(show_demo)
