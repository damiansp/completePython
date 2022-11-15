import asyncio
import sys

sys.path.append('..')
from util import async_timed, delay


@async_timed()
async def main():
    task1 = asyncio.create_task(cpu_work())
    task2 = asyncio.create_task(cpu_work())
    delay_task = asyncio.create_task(delay(4))
    await task1
    await task2
    await delay_task


@async_timed()
async def cpu_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


if __name__ == '__main__':
    asyncio.run(main())

