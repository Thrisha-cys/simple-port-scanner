import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    
    try:
        scanner.connect((ip, port))
        return True
    except:
        return False

def main():
    ip = input("Enter target IP address: ")
    print(f"\nScanning ports on {ip}...\n")

    for port in range(1, 101):  # scanning first 100 ports
        if scan_port(ip, port):
            print(f"Port {port} is OPEN")
        # else:
        #     print(f"Port {port} is closed")

    print("\nScan completed.")

if __name__ == "__main__":
    main()
