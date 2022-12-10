import asyncio
import sys

sys.path.append('..')
from util import delay


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

def call_later():
    print("I'll be called in the future!")


if __name__ == '__main__':
    asyncio.run(main())
    
