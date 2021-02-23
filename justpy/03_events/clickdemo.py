import justpy as jp


def clickit(self, msg):
    self.text = 'I have been clicked.'


def demo():
    wp = jp.WebPage()
    d = jp.Div(text='Unclicked',
               a=wp,
               classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', clickit)
    return wp


jp.justpy(demo)
