import socket
# run the server code first then the client code in another terminal by the command (python exercice1_client.py)
HOST = "127.0.0.1"  # The server IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")