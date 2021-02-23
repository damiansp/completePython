import justpy as jp


wp = jp.WebPage(delete_flag=False) # allow multiple renderings
p_style = ('w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2'
           'px-4 rounded')
for i in range(1, 11):
    jp.P(text=f'\n{i}) Hello, World!\n', a=wp, classes=p_style)


def hello():
    return wp


jp.justpy(hello)
