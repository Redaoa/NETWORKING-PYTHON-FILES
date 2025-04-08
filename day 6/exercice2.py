from scapy.all import sniff, DNS, DNSQR

def process_packet(packet):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:  # DNS query
        dns_query = packet.getlayer(DNSQR).qname.decode()
        print(f"DNS Query: {dns_query}")

# Capture DNS packets on the network interface (e.g., 'eth0')
# Replace 'eth0' with the correct interface name or omit 'iface' to use the default interface
sniff(filter="udp port 53", prn=process_packet, store=0)