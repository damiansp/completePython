import justpy as jp

wp = jp.WebPage()
p = jp.P(text='Hello, World!')
wp.add(p) # or p.add_to(wp); wp += p

wp2 = jp.WebPage()
p = jp.P(text='Hello, World!', a=wp) # same
