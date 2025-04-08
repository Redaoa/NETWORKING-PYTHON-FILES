import socket
import nmap

def detect_protocol_with_socket(ip, port):
    
        # Check TCP
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(1)
        result_tcp = tcp_socket.connect_ex((ip, port))
        if result_tcp == 0:
            tcp_socket.close()
            
            return "TCP"
        else:
            tcp_socket.close()
            return "UDP"