import asyncio


async def delay(s: int) -> int:
    print(f'Sleeping for {s}s...')
    await asyncio.sleep(s)
    print(f'{s}s sleep complete.')
    return s
