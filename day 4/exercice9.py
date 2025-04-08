import socket
import time

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error as e:
        print(f"Error resolving domain {domain}: {e}")
        return None

def check_ip_change(domain, interval=60, duration=3600):
    previous_ip = None
    start_time = time.time()
    
    while time.time() - start_time < duration:
        current_ip = get_ip(domain)
        if current_ip:
            if previous_ip and current_ip != previous_ip:
                print(f"IP address for {domain} has changed from {previous_ip} to {current_ip}")
            previous_ip = current_ip
        time.sleep(interval)

# Example usage
domain = "example.com"
check_ip_change(domain, interval=60, duration=3600)