import justpy as jp


def clickit(self, msg):
    self.text = 'I have been clicked.'
    self.set_class('bg-blue-500')


def mousein(self, msg):
    self.text = 'I smell a mouse'
    self.set_class('bg-red-500')


def mouseout(self, msg):
    self.text = 'No more mice'
    self.set_class('bg-teal-500')


def demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet',
               a=wp,
               classes='w-64 text-2xl m-2 p-2 bg-blue-500 text-white',
               click=clickit,
               mouseenter=mousein,
               mouseleave=mouseout)
    return wp


jp.justpy(demo)
