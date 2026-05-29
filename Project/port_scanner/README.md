# Python Port Scanner

A basic TCP port scanner built using Python sockets.

## Features
- TCP connection scanning
- Open port detection
- Configurable target and port range

## Concepts Learned
- Socket programming
- TCP communication
- Port scanning logic
- Network service detection

## Usage

```bash
python3 scanner.py
```
 - This is to be done after running a server of our own


## Versions
### V1           - deleted
 - Sequential search, very basic, but time consuming.
 - Need to improve searching, usage of asyncio and threading will be needed
 - PORT 135 was also open, it is the standard tcp/udp port for RPC endpoint mapper
 - PORT 445 was also open, primary port used by server message block SMB.

### V2
 - Added timeout, to make sure our search is faster
 - Made the whole file more modular, will be expanded in V3 via threading, and in many other versions to come
 - The scan range is also configurable now
 - Time showed Time taken: 101.30 seconds.

### V3       
 - Added MultiThreading
 - Improved the scan speed by a huge margin: 0.53 second. 
 - Basic concept for I/O-bound networking tasks
 - limitation tho: 1 thread per port, need to expand this in next model

### V4
 - Added user input support
 - Added configurable targets
 - Added configurable port ranges
 - Improved usability and flexibility

### V5 
 - Added banner grabbing
 - Attempted service identification on open ports
 - Learned basic application-layer interaction
 - Improved understanding of exposed network services
 - The output on running a ssh service in wsl
``` bash
 Enter the target IPaddress or HostName: localhost
Enter the starting port: 20
Enter the ending port: 25
Scanning localhost....

[OPEN] Port 22
   Banner: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.15
```