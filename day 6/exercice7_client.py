import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
client_socket.connect(server_address)

try:
    # Send data
    message = b'This is the message. It will be echoed back.'
    print('Sending:', message)
    client_socket.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print('Received:', data)

finally:
    # Clean up the connection
    client_socket.close()
