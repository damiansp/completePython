import asyncio
import sys

import aiohttp
from aiohttp import ClientSession

sys.path.append('..')
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://example.com', delay)
            for delay in [1, 10, 10]]
        for completed in asyncio.as_completed(fetchers, timeout=2):
            try:
                res = await completed
                print(res)
            except asyncio.TimeoutError:
                print('Got timed out!')
        for task in asyncio.tasks.all_tasks():
            print(task)


if __name__ == '__main__':
    asyncio.run(main())
