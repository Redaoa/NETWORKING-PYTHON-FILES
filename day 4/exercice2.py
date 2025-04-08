import socket

def reverse_dns_lookup(ip_address):
    try:
        result = socket.gethostbyaddr(ip_address)
        return result[0]
    except socket.herror :
        return None

ip = '8.8.8.8'
domain = reverse_dns_lookup(ip)
print(f"Domain for IP {ip}: {domain}")