import socket
import random
import os

os.system("clear")
print("//~~ Client Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

m = str(random.randint(1000, 2000))
sock.sendall(b"[1] SYN/seq=" + m.encode())

synack = sock.recv(1024).decode()
print(synack)

n = synack.split("seq=")[1].split(" ")[0]
n = str(int(n) + 1)
sock.sendall(b"[3] ACK/seq=" + n.encode())