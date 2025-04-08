from scapy.all import rdpcap, TCP

def extract_http_requests(pcap_file):
    packets = rdpcap(pcap_file)
    http_requests = []

    for packet in packets:
        if packet.haslayer(TCP) and packet[TCP].dport == 80:
            try:
                http_payload = bytes(packet[TCP].payload)
                if b"GET" in http_payload or b"POST" in http_payload:
                    http_requests.append(http_payload)
            except Exception as e:
                continue

    return http_requests

# Example usage
pcap_file = 'packet.pcap'
http_requests = extract_http_requests(pcap_file)
for request in http_requests:
    print(request.decode(errors='ignore'))
