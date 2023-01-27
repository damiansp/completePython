import asyncio
import sys

import aiohttp
from aiohttp import ClientSession

sys.path.append('..')
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as sess:
        urls = ['https://example.com'] * 1000
        requests = [fetch_status(sess, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


if __name__ == '__main__':
    asyncio.run(main())
