import socket
import sys

def scan_ports(target):
    print(f"[+] Scanning Host: {target}")
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    scan_ports(target_ip)
