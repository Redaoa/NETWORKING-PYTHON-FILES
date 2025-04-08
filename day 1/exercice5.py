import ipaddress
ip = ipaddress.ip_interface('192.168.1.10/24')
user_input = input("Enter the IP address and subnet mask (e.g., 192.168.1.10/24): ")
ip = ipaddress.ip_interface(user_input)
network = ip.network
broadcast_address = network.broadcast_address
network_address = network.network_address

print(f"Network Address: {network_address}")
print(f"Broadcast Address: {broadcast_address}")
