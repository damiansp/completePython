import asyncio

import aiohttp
from aiohttp import ClientSession


async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=0.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://example.com')

        
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_ms = aiohttp.ClientTimeout(total=0.01)
    async with session.get(url, timeout=ten_ms) as res:
        return res.status


if __name__ == '__main__':
    asyncio.run(main())
