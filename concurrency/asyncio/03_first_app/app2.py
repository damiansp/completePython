import asyncio
from asyncio import AbstractEventLoop
import logging
import signal
import socket
import sys
from typing import Set

sys.path.append('..')
from util import delay


tasks = []


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    #loop.add_signal_handler(
    #    signal.SIGINT, lambda asyncio.create_task(await_all_tasks()))
    loop.add_signal(singal.SIGINT, shutdown)
    await delay(10)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    await listen_for_conn(server_socket, asyncio.get_event_loop())


def cancel_tasks():
    print('Got SIGINT')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} task(s)')
    [task.cancel() for task in tasks]


async def await_all_tasks():
    tasks = asyncio.all_tasks()
    [await task for task in tasks]
    
    
async def echo(conn: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(conn, 1024):
            if data == b'boom\r\n':
                raise Exception('Unexpected network error')
            await loop.sock_sendall(conn, data)
    except Exception as e:
        logging.exception(e)
    finally:
        connection.close()


async def listen_for_conn(server_socket: socket, loop: AbstractEventLoop):
    while True:
        conn, address = await loop.sock_accept(server_socket)
        conn.setblocking(False)
        print(f'Got connection from {address}')
        tasks.append(asyncio.create_task(echo(conn, loop)))


class GracefulExit(SystemExit):
    pass


def shutdoiwn():
    raise GracefulExit()




if __name__ == '__main__':
    asyncio.run(main())
