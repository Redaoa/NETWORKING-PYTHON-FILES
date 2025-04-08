import socket
import random
import os

os.system("clear")
print("//~~ Server Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

(client, (host, port)) = sock.accept()

syn = client.recv(1024).decode()
print(syn)

m = syn.split("seq=")[1]
m = str(int(m) + 1)
n = str(random.randint(1000, 2000))
client.sendall(b"[2] SYN/seq=" + n.encode() + b" ACK/seq=" + m.encode())

ack = client.recv(1024).decode()
print(ack)