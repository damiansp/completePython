import asyncio
import sys

sys.path.append('..')
from util import delay


async def hello_every_second(reps=3):
    for i in range(reps):
        await asyncio.sleep(1)
        print("Hi, I'm running other code while I wait...")


async def main():
    delay_1 = asyncio.create_task(delay(3))
    delay_2 = asyncio.create_task(delay(3.5))
    await hello_every_second()
    await delay_1
    await delay_2


if __name__ == '__main__':
    asyncio.run(main())
