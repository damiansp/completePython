import asyncio
import sys

sys.path.append('..')
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        res = await asyncio.wait_for(delay_task, timeout=1)
        print(res)
    except asyncio.exceptions.TimeoutError:
        print('Timed out!')
        print(f'Cancelled: {delay_task.cancelled()}')


if __name__ == '__main__':
    asyncio.run(main())
