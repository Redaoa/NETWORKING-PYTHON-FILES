import ipaddress
ip = ipaddress.ip_address('192.168.1.1')
binary_form = '{:#b}'.format(ip)
print(f'The binary form of the IP address is: {binary_form}')