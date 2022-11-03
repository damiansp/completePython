import asyncio
import sys

sys.path.append('..')
from util import delay


async def main():
    sleep_3 = asyncio.create_task(delay(3))
    print(type(sleep_3))  # _asyncio.Task
    res = await sleep_3
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
