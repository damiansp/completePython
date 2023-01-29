import asyncio
import sys

import aiohttp
from aiohttp import ClientSession

sys.path.append('..')
from util import async_timed


async def fetch_status(session: ClientSession, url: str, delay: int=0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as sess:
        fetchers = [
            fetch_status(sess, 'http://www.example.com', delay)
            for delay in [1, 1, 10]]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


if __name__ == '__main__':
    asyncio.run(main())
