from scapy.all import rdpcap, TCP
import re
def extract_http_requests(pcap_file):
    packets = rdpcap(pcap_file)
    http_requests = []

    for packet in packets:
        if packet.haslayer(TCP) and packet[TCP].dport == 80:
            try:
                http_payload = bytes(packet[TCP].payload)
                if b"GET" in http_payload or b"POST" in http_payload:
                    http_requests.append(http_payload)
                    with open("http.txt", "a") as file:
                        file.write(http_payload.decode(errors="ignore") + "\n")
            except Exception as e:
                continue
            



def extract_urls_from_http_requests(http_requests_file):
    
    with open(http_requests_file, 'r') as file:
        text = file.read()

    # Regular expression to match URLs
    url_pattern = r'https?://\S+'
    urls = re.findall(url_pattern, text)

    # Print or save the URLs
    print("Extracted URLs:")
    for url in urls:
        print(url)

http_requests_file = extract_http_requests('file.pcap') # Replace 'file.pcap' with the actual path to your pcap file
extract_urls_from_http_requests(http_requests_file)