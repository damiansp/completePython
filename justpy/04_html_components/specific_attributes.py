import justpy as jp


def html_comps():
    wp = jp.WebPage()
    for degree in range(0, 361, 10):
        image = jp.Img(
            src=('https://www.python.org/static/community_logos/python-powered-'
                 'h-140x182.png'),
            a=wp)
        image.classes = 'm-4 p-4 inline-block'
        image.style = f'transform: rotate({degree}deg)'
        image.height = 100
        image.width = 100
        image.degree = degree
        image.on('mouseenter', straighten)
        image.on('mouseleave', rotate_back)
        image.on('click', no_rotate)
    return wp


def straighten(self, msg):
    self.style = 'transfrom: rotate(0deg)'

    
def rotate_back(self, msg):
    self.style = f'transform: rotate({self.degree}deg)'

    
def no_rotate(self, msg):
    self.degree = 0
    self.set_class('bg-red-200')


jp.justpy(html_comps)
