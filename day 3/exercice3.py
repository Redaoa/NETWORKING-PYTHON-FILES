import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'  # Listen on all available interfaces
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    client_socket.send("hell. client!")
