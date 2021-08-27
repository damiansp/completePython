import justpy as jp


html = '''
<div class="bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md" 
     role="alert">
  <div class="flex">
    <div class="py-1">
      <svg class="fill-current h-6 w-6 text-teal-500 mr-4" 
           xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
        <path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"
        />
      </svg>
    </div>
    <div>
      <p class="font-bold">Our privacy policy has changed</p>
      <p class="text-sm">Make sure you know how these changes affect you.</p>
    </div>
  </div>
</div>
'''

d = jp.parse_html(html)
for c in d.commands:
    print(c)


BL = 'font-bold text-lg'
DIV = ('bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 '
       'py-3 shadow-md')
MW = 'm-2 w-1/4'
PATH = ('M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 '
        'n17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 '
        '11V9h2v6H9v-4zm0-6h2v2H9V5z')
SVG = 'fill-current h-6 w-6 text-teal-500 mr-4'


class MyAlert(jp.Div):
    def __init__(self, **kwargs):
        self.title_text = 'This is the Title'
        self.body_text = 'This is the Body'
        super().__init__(**kwargs)
        root = self
        c1 = jp.Div(classes=DIV, role='alert', a=root)
        c2 = jp.Div(classes='flex', a=c1)
        c3 = jp.Div(classes='py-1', a=c2)
        c4 = jp.Svg(classes=SVG,
                    xmlns='http://www.w3.org/2000/svg',
                    viewBox='0 0 20 20',
                    a=c3)
        c5 = jp.Path(d=PATH, a=c4)
        c6 = jp.Div(a=c2)
        c7 = jp.P(classes=BL, a=c6, text=self.title_text)
        c8 = jp.P(classes='text-sm', a=c6, text=self.body_text)


def alert_test():
    wp = jp.WebPage()
    d = MyAlert(
        a=wp, classes=MW, title_text='Hello!', body_text='How do you do?')
    d.title_text = 'Shalom!' # why does this do nothing?
                             # - attr need to be assigned at render time, not
                             #   creation time.... see react_method.py
    return wp


jp.justpy(alert_test)

