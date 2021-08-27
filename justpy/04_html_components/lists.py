import justpy as jp


def list_demo():
    wp = jp.WebPage()
    my_list = jp.Ul(a=wp, classes='m-2 p-2')
    for i in range(1, 11):
        jp.Li(text=f'L1 item {i}', a=my_list)
    list_two = jp.Ul(a=wp, classes='m-2 p-2 list-disc list-inside')
    for i in range(1, 11):
        jp.Li(text=f'L2 item {i}', a=list_two, classes='hover:bg-gray-200')
    list_three = jp.Ul(a=wp, classes='m-2 p-2 list-decimal list-inside')
    for i in range(1, 11):
        jp.Li(text=f'L3 item {i}', a=list_three)
    return wp


jp.justpy(list_demo)
        
