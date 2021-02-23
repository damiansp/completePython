import justpy as jp


def clickit(self, msg):
    self.text = 'I am clicked'
    print(msg.event_type)    # click
    print(msg['event_type']) # same
    print(msg)               # many other values


def demo():
    wp = jp.WebPage()
    d = jp.P(
        text='Unclicked', a=wp, classes='text-xl m-2 p-2 bg-blue-500 text-white'
    )
    d.on('click', clickit)
    return wp


jp.justpy(demo)
