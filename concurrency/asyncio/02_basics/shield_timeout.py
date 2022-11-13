import asyncio
import sys

sys.path.append('..')
from util import delay


async def main():
    task = asyncio.create_task(delay(10))
    try:
        res = await asyncio.wait_for(asyncio.shield(task), 5)
        print(res)
    except asyncio.exceptions.TimeoutError:
        print('Task took longer than 5s, but should finish soon!')
        res = await task
        print(res)


if __name__ == '__main__':
    asyncio.run(main())
