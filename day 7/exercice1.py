import nmap
import ipaddress
def scan_ports(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1000')

    open_ports = []
    if ip in nm.all_hosts():
        for port in nm[ip]['tcp']:
            if nm[ip]['tcp'][port]['state'] == 'open':
                open_ports.append(port)

    return open_ports

beginning_ip = '192.168.1.1'
ending_ip = '192.168.1.50'
network = ipaddress.summarize_address_range(
    ipaddress.IPv4Address(beginning_ip), ipaddress.IPv4Address(ending_ip)
)

for subnet in network:
    for ip in subnet:
        try:
            open_ports = scan_ports(str(ip))
            print(f"Open ports on {ip}: {open_ports}")
        except Exception as e:
            print(f"Error scanning {ip}: {e}")