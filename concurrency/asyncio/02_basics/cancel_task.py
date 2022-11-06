import asyncio
from asyncio import CancelledError
import sys

sys.path.append('..')
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    s_elapsed = 0
    while not long_task.done():
        print('Task incomplete, checking again in a second...')
        await asyncio.sleep(1)
        s_elapsed += 1
        if s_elapsed == 5:
            print('Canceling task...')
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Task was cancelled')


if __name__ == '__main__':
    asyncio.run(main())
    
