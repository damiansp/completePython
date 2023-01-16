import asyncio
import sys

import aiohttp
from aiohttp import ClientSession

sys.path.append('..')
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as res:
        return res.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Status for {url}: {status}')


if __name__ == '__main__':
    asyncio.run(main())
