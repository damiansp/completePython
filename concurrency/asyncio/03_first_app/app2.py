import asyncio
from asyncio import AbstractEventLoop
import socket


async def echo(conn: socket, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(conn, 1024):
        await loop.sock_sendall(conn, data)


async def listen_for_conn(server_socket: socket, loop: AbstractEventLoop):
    while True:
        conn, address = await loop.sock_accept(server_socket)
        conn.setblocking(False)
        print(f'Got connection from {address}')
        asyncio.create_task(echo(conn, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    await listen_for_conn(server_socket, asyncio.get_event_loop())


if __name__ == '__main__':
    asyncio.run(main())
