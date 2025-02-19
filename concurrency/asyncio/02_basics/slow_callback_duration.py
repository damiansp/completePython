import asyncio


async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 0.250


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
