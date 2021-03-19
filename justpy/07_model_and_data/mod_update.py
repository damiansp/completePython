import justpy as jp


CORNER = 'p-3 absolute bg-gray-200'
DIV = 'relative h-screen bg-gray-600'
INPUT = 'absolute text-xl border-2 border-red-600'


def demo():
    wp = jp.WebPage()
    d = jp.Div(classes=DIV, a=wp, data={'text': ''})
    repeat = 1
    for vpos in ['top', 'bottom']:
        for hpos in ['left', 'right']:
            corner_div = jp.Div(classes=f'{CORNER} {vpos}-0 {hpos}-0', a=d)
            jp.Div(text=f'{vpos} {hpos}', a=corner_div)
            MyDiv(text='Typing goes here',
                  a=corner_div,
                  model=[d, 'text'],
                  repeat=repeat,
                  initial_text='Yada Yada')
    middle_input = jp.Input(text='middle',
                            classes=INPUT,
                            placeholder='Type here',
                            style='top: 50%; left: 40%',
                            model=[d, 'text'],
                            a=d)
    return wp


class MyDiv(jp.Div):
    def model_update(self):
        # mod has form [wp, 'text'] (e.g.)
        if self.model[0].data[self.model[1]]:
            self.text = self.repeat * (
                str(self.model[0].data[self.model[1]]) + ' ')
        else:
            self.text = self.initial_text


jp.justpy(demo)
