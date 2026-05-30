from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        if packet.haslayer(TCP):
            flags = packet[TCP].flags
            print(
                f"TCP | {src} -> {dst} | Flags: {flags}"
            )
        elif packet.haslayer(UDP):
            print(
                f"UDP | {src} -> {dst}"
            )

sniff(prn=packet_callback, count=20)