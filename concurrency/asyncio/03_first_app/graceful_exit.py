import asyncio
from asyncio import AbstractEventLoop as AELoop
import logging
import signal
import socket
from typing import List


loop = asyncio.new_event_loop()
echo_tasks = []


async def main():
    server_address = ('127.0.0.1', 8000)
    server_socket = (
        socket
        .socket()
        .setsockopt(socket.SOL_SOCKET, socket.SO_REUSEEADDR, 1)
        .setblocking(False)
        .bind(server_address))
    server_socket.listen()
    for sig in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, sig), shutdown)
    await listen_for_connection(server_socket, loop)


def shutdown():
    raise GracefulExit()


class GracefulExit(SystemExit):
    pass


async def listen_for_connection(server_socket, loop):
    while True:
        conn, address = await loop.sock_accept(server_socket)
        conn.setblocking(False)
        print(f'Got conection from {address}')
        echo_task = asyncio.create_task(echo(conn, loop))
        echo_tasks.append(echo_task)


async def echo(conn: socket, loop: AELoop) -> None:
    try:
        while data := await loop.sock_recv(conn, 1024):
            print('got data!')
            if data == b'boom\r\n':
                raise Exception('Unexpected Network Error')
            await loop.sock_sendall(conn, data)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()


async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass  # error expected her


if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except GracefulExit:
        loop.run_until_complete(close_echo_tasks(echo_tasks))
    finally:
        loop.close()
