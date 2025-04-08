import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
server_socket.bind(server_address)

server_socket.listen(1)

print('Waiting for a connection...')
connection, client_address = server_socket.accept()

try:
    print('Connection from', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(16)
        if data:
            print('Received:', data)
            connection.sendall(data)
        else:
            break

finally:
    # Clean up the connection
    connection.close()
