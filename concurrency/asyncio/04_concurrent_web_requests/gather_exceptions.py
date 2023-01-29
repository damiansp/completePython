import asyncio
import sys

imort aiohttp


sys.path.append('..')
from util import async_timed, fetch_status_code


@async_timed()
async def main():
    async with aiohttp.ClientSession() as sess:
        urls = ['https://example.com', 'bad_url://example.com']
        tasks = [fetch_status_code(sess, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        exceptions = [res for res in results if isintance(res, BaseException)]
        statuses = [res for res in results if not isintance(res, BaseException)]
        print(f'All results: {results}')
        print(f'Successful: {statuses}')
        print(f'Exceptions: {exceptions}')
        
