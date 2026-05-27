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
### V1
 - Sequential search, very basic, but time consuming.
 - Need to improve searching, usage of asyncio and threading will be needed
 - PORT 135 was also open, it is the standard tcp/udp port for RPC endpoint mapper
 - PORT 445 was also open, primary port used by server message block SMB.

### V2

