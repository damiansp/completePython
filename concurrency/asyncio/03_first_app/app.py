import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)
connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Connection made with {client_address}')
            connections.append(connection)
        except BlockingIOError:
            pass
        for connection in connections:
            try:
                buff = b''
                while buff[-2:] != '\r\n':
                    data = connection.recv(2)
                    if data:
                        print(f'Got data: {data}!')
                        buff += data
                    else:
                        break
                print(f'Complete data:\n{buff}')
                connection.sendall(buff)
            except BlockingIOError:
                pass
finally:
    server_socket.close()
