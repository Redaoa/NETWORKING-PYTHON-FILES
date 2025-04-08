from kamene.all import *
from kamene.layers.inet import IP, TCP
from kamene.volatile import RandShort

iplayer = IP(dst="47.95.194.185", id=1111, ttl=99)
tcplayer = TCP(sport=RandShort(), dport=[80], seq=12345, ack=1000, window=1000, flags="S")
packet = iplayer / tcplayer
send(packet)