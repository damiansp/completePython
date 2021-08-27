import justpy as jp


PILL = 'bg-%s-500 hover:bg-%s-700 text-white font-bold py-2 px-4 rounded-full'


def test():
    wp = jp.WebPage()
    for color in ['blue', 'red', 'orange', 'pink']:
        PillButton(bg_color=color,
                   text='The Pill',
                   click='self.text="I am clicked"',
                   a=wp,
                   classes='m-2')
    return wp


class PillButton(jp.Button):
    bg_color = 'blue'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_classes(PILL % (self.bg_color, self.bg_color))
        
    
jp.justpy(test)
