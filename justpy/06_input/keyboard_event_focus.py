import justpy as jp


DIV = 'flex flex-col m-2'


def focus_test():
    wp = jp.WebPage()
    d = jp.Div(classes=DIV, a=wp, style='width: 600px')
    input_list = []
    n_fields = 5
    for i in range(1, n_fields + 1):
        label = jp.Label(a=d, classes='m-2 p-2')
        jp.Span(text=f'Field {i}', a=label)
        in1 = jp.Input(classes=jp.Styles.input_classes,
                       placeholder=f'{i} Type here',
                       a=label,
                       keydown=key_down,
                       spellcheck='false')
        in1.on('blur', blur)
        in1.input_list = input_list
        in1.n = i - 1
        input_list.append(in1)
    return wp


def key_down(self, msg):
    key = msg.key_data.key
    if key == 'Escape':
        self.value = ''
        return
    if key == 'Enter':
        self.set_focus = False
        try:
            next_to_focus = self.input_list[self.n + 1]
        except:
            next_to_focus = self.input_list[0]
        next_to_focus.set_focus = True
        return
    return True


def blur(self, msg):
    self.set_focus = False


jp.justpy(focus_test)
