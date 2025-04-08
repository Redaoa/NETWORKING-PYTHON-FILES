from scapy.all import sniff, TCP, Raw
import re

def monitor_post_requests(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if "POST" in payload:
            print("Captured POST request:")
            print(payload)
            print("-" * 50)

# Sniff packets on the default network interface
print("Monitoring outgoing POST requests...")
sniff(filter="tcp port 80", prn=monitor_post_requests, store=False)