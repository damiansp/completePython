import justpy as jp


def comp_test():
    wp = jp.WebPage()
    d = jp.Div(
        text='Hello 1',
        click='self.text="clicked"',
        mouseenter=(
            'self.text="entered"; self.set_class("text-5xl"); '
            'msg.page.add(Div(text=f"{len(msg.page)} Additional Div"))'),
        mouseleave='self.text="left"; self.set_class("text-xl")',
        classes='text-2xl border p-2 m-2',
        a=wp)
    d = jp.Div(text='Hello 2',
               click='self.text="clicked"',
               mouseenter='self.text="entered"',
               classes='text-2xl border p-2 m-2',
               a=wp)
    d = jp.Div(text='Hello 3',
               click='self.text="clicked"',
               mouseenter='self.text="entered"',
               classes='text-2xl border p-2 m-2',
               a=wp)
    return wp


jp.justpy(comp_test)
