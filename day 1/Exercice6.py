import ipaddress

def calculate_ips(subnet):
    
     network = ipaddress.ip_network(subnet, strict=False)
     return [str(ip) for ip in network.hosts()]
    

subnet = '192.168.1.1/24'
all_ips = calculate_ips(subnet)
print(all_ips)