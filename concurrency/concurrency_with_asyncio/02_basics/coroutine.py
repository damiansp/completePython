import asyncio


async def hello_coroutine() -> None:
    print('Hello, World!')


async def add_one_co(n: int) -> int:
    return n + 1


def add_one(n: int) -> int:
    return n + 1


def main():
    func_res = add_one(1)
    co_res = add_one_co(1)
    print(f'Function result is {func_res}, of type {type(func_res)}')
    print(f'Coroutine result is {co_res}, of type {type(co_res)}')
    async_res = asyncio.run(add_one_co(1))
    print(f'Aysnc coroutine result is {async_res}, of type {type(async_res)}')

if __name__ == '__main__':
    main()
