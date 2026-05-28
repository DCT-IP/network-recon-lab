import socket 
import time
TARGET = "127.0.0.1" #local host
START_PORT = 7900
END_PORT = 8100

def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) #to allow the scan to complete faster
    result = sock.connect_ex((TARGET, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    sock.close()

print(f"Scanning {TARGET}....\n")
start_time = time.time()
for port in range(START_PORT, END_PORT + 1):
    scan(port)
end_time = time.time()
print(f"\nScan complete. Time taken: {end_time - start_time:.2f} seconds.")