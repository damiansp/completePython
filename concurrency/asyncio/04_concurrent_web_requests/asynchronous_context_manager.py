import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    async with ConnectedSocket(server_socket) as conn:
        data = await loop.sock_recv(conn, 1024)
        print(data)
        
    
class ConnectedSocket:
    def __init__(self, server_socket):
        self._conn = None
        self._server_socket = server_socket

    async def __aenter__(self):
        print('Entering context manager. Waiting for connection...')
        loop = asyncio.get_event_loop()
        conn, address = await loop.sock_accept(self._server_socket)
        self._conn = conn
        print('Connection accepted')
        return self._conn

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optiona[TracebackType]):
        print('Exiting context manager...')
        self._conn.close()
        print('Connection closed')


if __name__ == '__main__':
    asyncil.run(main())
