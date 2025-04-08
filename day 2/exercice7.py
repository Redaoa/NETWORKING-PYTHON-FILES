import socket

for port in range(1, 65535):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        if not s.connect_ex(('127.0.0.1', port)):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")