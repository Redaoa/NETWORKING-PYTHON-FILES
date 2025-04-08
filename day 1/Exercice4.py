import ipaddress
ip = ipaddress.ip_address('192.168.0.1')
globality = ip.is_global
if globality == True:
    print("The IP address is global.")
else:
    print("The IP address is private.")