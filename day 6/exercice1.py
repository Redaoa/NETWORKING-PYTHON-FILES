from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Capture outgoing packets on the default interface
sniff(filter="ip", prn=packet_callback, store=0)