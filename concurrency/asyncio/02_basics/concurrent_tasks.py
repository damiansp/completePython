import asyncio
import sys

sys.path.append('..')
from util import delay


async def main():
    sleep_3 = asyncio.create_task(delay(3))
    sleep_3_more = asyncio.create_task(delay(3))
    sleep_3_final = asyncio.create_task(delay(3))
    await sleep_3
    await sleep_3_more
    await sleep_3_final


if __name__ == '__main__':
    asyncio.run(main())
