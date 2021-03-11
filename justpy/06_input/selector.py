import justpy as jp


SELECT = 'w-32 text-xl m-4 p-2 bg-white  border rounded'
DIV = 'bg-red-600 w-32 h-16 m-4'


def comp_test():
    wp = jp.WebPage()
    colors = ['blue', 'green', 'pink', 'purple', 'red', 'teal', 'yellow']
    select = jp.Select(classes=SELECT, a=wp, value='blue', change=change_color)
    for color in colors:
        select.add(
            jp.Option(value=color, text=color, classes=f'bg-{color}-600'))
    select.color_div = jp.Div(classes=DIV, a=wp)
    return wp


def change_color(self, msg):
    self.color_div.set_class(f'bg-{self.value}-600')


jp.justpy(comp_test)
