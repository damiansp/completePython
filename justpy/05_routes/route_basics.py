import justpy as jp


def hello():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello, World!', classes='text-5xl m-2'))
    return wp


def goodbye():
    wp = jp.WebPage()
    wp.add(jp.P(text='Goodbye!', classes='text-5xl m-2'))
    return wp

jp.Route('/hello', hello)
jp.justpy(goodbye)
           
