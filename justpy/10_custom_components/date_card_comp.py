import justpy as jp


CALENDAR_DATE = '''
<div 
  class="w-24 rounded-t overflow-hidden bg-white text-center m-2 cursor-default"
>
  <div class="bg-%s-500 text-white py-1">%s</div>
  <div class="pt-1 border-l border-r">
    <span class="text-4xl font-bold">%s</span>
  </div>
  <div 
    class="pb-2 px-2 border-l border-r border-b rounded-b flex justify-between">
    <span class="text-xs font-bold">%s</span>
    <span class="text-xs font-bold">%s</span>
  </div>
</div>
'''
FFW = 'flex flex-wrap'


class CalendarDate(jp.Div):
    def __init__(self, **kwargs):
        self.month = 'Jan'
        self.year = '2021'
        self.weekday = 'Fri'
        self.day = '1'
        self.color = 'red'
        super().__init__(**kwargs)
        self.inner_html  = CALENDAR_DATE % (
            self.color, self.month, self.day, self.weekday, self.year)


def comp_test():
    wp = jp.WebPage()
    year = 2020
    month = 'Apr'
    d = jp.Div(classes=FFW, a=wp)
    for day in range(1, 11):
        CalendarDate(day=day,
                     month=month,
                     year=year,
                     color='teal',
                     a=d,
                     animation='bounceIn')
    d = jp.Div(classes=FFW, a=wp)
    for day in range(5, 26):
        CalendarDate(day=day, month='Jul', year='2005', color='yellow', a=d)
    return wp


jp.justpy(comp_test)
