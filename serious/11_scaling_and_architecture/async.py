import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as response:
            return response

loop = asyncio.get_event_loop()
coroutines = [get('http://example.com') for _ in range(8)]
res = loop.run_until_complete(asyncio.gather(*coroutines))
print(f'Results: {res}\nLength: {len(res)}')
