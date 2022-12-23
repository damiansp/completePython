import selectors
from selectors import SelectorKey
import socket
from typing import List, Tuple


selector = selctors.DefaultSelctor()
server_socket = socket.socket() #(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(False)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)


while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
    if not len(events):
        print('No events, still waiting...')
    for event, _ in events:
        if event_socket == server_socket:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Connection made with {client_address}')
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f'Got some data: {data}')
            event_socket.send(data)
