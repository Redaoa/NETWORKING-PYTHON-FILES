from scapy.all import ARP, Ether, srp

def get_mac_addresses(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Adjust the IP range as needed
    devices = get_mac_addresses(ip_range)
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")