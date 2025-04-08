import ipaddress
def ip_class_organisator(ip):
    ip = ipaddress.ip_address(ip)
    first_octet = int(str(ip).split('.')[0])
    if first_octet < 128:
        return 'A'
    elif first_octet < 192:
        return 'B'
    elif first_octet < 224:
        return 'C'
    elif first_octet < 240:
        return 'D'
    else:
        return 'E'
ip = input ('Enter an IP address: ')
ip_class = ip_class_organisator(ip)
print(f'the ip class is {ip_class} class')