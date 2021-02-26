# click__out fires when you click outside an element
import justpy as jp


def clickout(self, msg):
    self.text = 'click out'
    self.set_classes('text-blue-500')


def clickin(self, msg):
    self.text = 'click in'
    self.set_classes('text-red-500')


def test():
    wp = jp.WebPage()
    for i in range(4):
        d = jp.Div(
            text=f'{i}) Div', a=wp, classes='m-4 p-4 text-xl border w-32')
        d.on('click__out', clickout)
        d.on('click', clickin)
    return wp


jp.justpy(test)
