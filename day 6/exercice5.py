from scapy.all import ARP, sniff, sr

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP reply
        real_mac = getmacbyip(packet[ARP].psrc)
        response_mac = packet[ARP].hwsrc

        if real_mac and real_mac != response_mac:
            print(f"[ALERT] ARP Spoofing detected! IP: {packet[ARP].psrc}, Real MAC: {real_mac}, Fake MAC: {response_mac}")

def getmacbyip(ip):
    try:
        ans, _ = sr(ARP(pdst=ip), timeout=2, verbose=False)
        for _, rcv in ans:
            return rcv[ARP].hwsrc
    except Exception as e:
        return None

print("Starting ARP spoofing detection...")
sniff(store=False, prn=detect_arp_spoof)