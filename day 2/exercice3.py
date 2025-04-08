import nmap

def scan_ports(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1000')

    open_ports = []
    for port in nm[ip]['tcp']:
        if nm[ip]['tcp'][port]['state'] == 'open':
            open_ports.append(port)

    return open_ports
  
ip_address = '192.168.1.1'  # Replace with your target IP address
open_ports = scan_ports(ip_address)
print(f"Open ports on {ip_address}: {open_ports}")
