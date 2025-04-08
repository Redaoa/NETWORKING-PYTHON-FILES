import ipaddress
ip = ipaddress.ip_address('192.168.1.1')

is_ipv4 = ip.version
if is_ipv4 == 4:
    print("your ip version is IPv4")
else:
    print("your ip version is IPv6")