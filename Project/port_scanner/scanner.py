import socket
target = "127.0.0.1"
print(f"Scanning {target}...\n")
for port in range(1, 10001):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))
    print(f"Scanning port {port}...")
    if result == 0:
        print(f"[OPEN] Port {port}")
    sock.close()
print("\nScan complete.")

