import justpy as jp


def clickit(self, msg):
    print(msg)
    self.text = 'I am clicked'


def demo():
    wp = jp.WebPage()
    wp.debug = True
    d = jp.Div(text='Not clicked yet',
               a=wp,
               classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', clickit)
    d.additional_properties = [
        'screenX', 'pageY', 'altKey', 'which', 'movementX', 'button', 'buttons']
    return wp


jp.justpy(demo)
