import justpy as jp


def hello_test():
    wp = jp.WebPage()
    h = jp.Hello()
    for i in range(5):
        wp.add(h)          # dependent comps
    for i in range(5):
        wp.add(jp.Hello()) # indep comps
    return wp


jp.justpy(hello_test)
