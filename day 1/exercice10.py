import ipaddress
ip1 = ipaddress.ip_address('192.168.1.15')
ip1_first_octet = int(str(ip1).split('.')[0])
ip2 = ipaddress.ip_address('192.168.1.19')
ip2_first_octet = int(str(ip2).split('.')[0])
if ip1_first_octet == ip2_first_octet:
    print('The two IP addresses are in the same subnet')
else:
    print('The two IP addresses aren\'t in the same subnet')