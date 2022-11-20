import asyncio
import requests
import sys

sys.path.append('..')
from util import async_timed


@async_timed()
async def main():
    # requests in blocking, so no gain by attempting async here
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3 = asyncio.create_task(get_example_status())
    await task1
    await task2
    await task3


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


if __name__ == '__main__':
    asyncio.run(main())
