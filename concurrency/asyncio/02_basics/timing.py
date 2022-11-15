import asyncio
import time

from time_decorator import async_timed


@async_timed()
async def main():
    task1 = asyncio.create_task(delay(2))
    task2 = asyncio.create_task(delay(3))
    await task1
    await task2


@async_timed()
async def delay(s: int) -> int:
    print(f'Sleeping for {s} second(s)')
    await asyncio.sleep(s)
    print(f'{s}-second nap complete.')
    return s


if __name__ == '__main__':
    asyncio.run(main())
