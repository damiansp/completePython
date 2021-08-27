# Tailwind ref: https://tailwindcss.com/
import justpy as jp


def hello():
    wp = jp.WebPage()
    p_design = ('w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold'
                'py-2 px-r rounded')
    for i in range(1, 11):
        jp.P(text=f'{i}) Hello, World!', a=wp, classes=p_design)
    return wp


jp.justpy(hello)
