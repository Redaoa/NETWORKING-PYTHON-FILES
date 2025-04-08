import socket

UDP_IP = "<ip_address_of_receiver>"
UDP_PORT = 8543
MESSAGE = "Hi, can you listen to this?"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))