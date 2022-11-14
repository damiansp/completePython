import asyncio
from asyncio import Future


async def main():
    my_future = Future()
    print(f'Future done: {my_future.done()}')
    my_future.set_result(42)
    print(f'Future done: {my_future.done()}')
    print(f'Future result: {my_future.result()}')


if __name__ == '__main__':
    asyncio.run(main())
