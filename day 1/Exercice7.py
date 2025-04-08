import os
def ping(ip):
    ping = os.system(f'ping -c 4 {ip}')
    if ping == 0:
        return True
    else:
        return False
print(ping('192.168.1.1'))