import asyncio
import time

import justpy as jp


CLOCK = 'text-5xl m-1 p-1 bg-gray-300 font-mono'

wp = jp.WebPage(delete_flag=False)
clock_span = jp.Span(text='Loading...', classes=CLOCK, a=wp)


async def clock():
    return wp


async def init_clock():
    jp.run_task(clock_counter())
    

async def clock_counter():
    while True:
        clock_span.text = time.strftime('%a, %d %b %Y, %H:%M:%S',
                                        time.localtime())
        jp.run_task(wp.update())
        await asyncio.sleep(1)
        

jp.justpy(clock, startup=init_clock)
