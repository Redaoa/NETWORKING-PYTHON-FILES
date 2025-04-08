import socket

BROADCAST_IP = '255.255.255.255'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', PORT))

print(f"Listening for broadcast messages on port {PORT}...")

try:
    while True:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode('utf-8')}")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    sock.close()
