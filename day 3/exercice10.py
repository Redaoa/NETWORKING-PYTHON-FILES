from scapy.all import sniff, DNS, TCP

def dns_callback(packet):
    if packet.haslayer(DNS):
        dns_layer = packet.getlayer(DNS)
        print(f"DNS Request: {dns_layer.qd.qname}")

sniff(filter="udp port 53", prn=dns_callback, store=0)

def tcp_callback(packet):
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")

sniff(filter="tcp", prn=tcp_callback, store=0)
