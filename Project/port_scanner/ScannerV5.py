import socket 
import threading 
import time 

TARGET = input("Enter the target IPaddress or HostName: ")
START_PORT = int(input("Enter the starting port: "))
END_PORT = int(input("Enter the ending port: "))

def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) #to allow the scan to complete faster
    result = sock.connect_ex((TARGET, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
        try:
            banner = sock.recv(1024).decode().strip()
            if banner:
                print(f"   Banner: {banner}")
        except:
            print(f"{banner}   No banner received.")
    sock.close()


print(f"Scanning {TARGET}....\n")
start_time = time.time()
threads = []

for port in range(START_PORT, END_PORT + 1):
    thread = threading.Thread(target=scan, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
end_time = time.time()
print(f"\nScan complete. Time taken: {end_time - start_time:.2f} seconds.")