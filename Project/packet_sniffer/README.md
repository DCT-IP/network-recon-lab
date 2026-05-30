# Packet Sniffer 

## Observation
Captured live TCP traffic using Scapy.
Observed:
 - SA (SYN ACK)
 - A (ACK)
 - PA (PSH ACK)
 - Raw payload packets

## Key Learning
TCP communication occurs in phases:
1. Handshake
   - SYN
   - SYN ACK
   - ACK

2. Data Transfer
   - PSH ACK packets carrying payload

3. Connection Termination
   - FIN ACK (not observed during this capture)

## Concepts Learned
- Packet sniffing
- TCP flags
- TCP handshake
- Client-server communication
- Application data transmission

## Versions
 ### V1
    - a basic scannner
    - gave packets for a limited period, pre-deteriment
    
 ### V2
    - Extracted source and destination IP addresses
    - Identified TCP and UDP packets
    - Parsed TCP flags
    - Improved packet readability