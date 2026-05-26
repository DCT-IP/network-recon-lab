# Nmap - Basics 
 - Network Mapper is an open source tool for network exploration and security auditing.
 - It scans large networks, uses raw IP packets in novel ways to determine what hosts are avaialbe on the network.

## Certain Concepts 

 - Ports: logical identifier used to distinguish diff applications or services on a device. Some examples
               1. 80: HTTP
               2. 25: SMTP
               3. 443: HTTPS
               4. 53: DNS
               5. 22: ssh

 - `-sV` is to identify running service versions
 - `-p` is to specify ports
 - while making a python server to bind it to a specifc IP we can write --bind <IP>
---

## Scans
### Initial Scans
 - Scanned localhost(inside WSL) when no services were running, thus it showed 
 ``` bash
    All 1000 scanned ports on localhost are closed
 ```
 - On performing
     ``` bash
        nmap -sV localhost
    ```
 - We got similar results as above

### Post Python HTTP Server
 - Ran initially a python3 server(localhost:8000) in windows, this gave the output
 ``` bash 
     port      STATE     Service
    8000/tcp   closed    https-alt
 ```
 - This was because WSL has its own virtualized networking layer, this causes windows localhost != wsl localhost
 - Then ran a python3 server(localhost:8000) in WSL, this gave the output
 ``` bash 
     port      STATE     Service   Version
    8000/tcp   open       http    SimpleHTTPServer 0.6 (python's version)
 ```
 - This confirmed that nmap detected the service

---

## Use cases for Nmap
 - Host discovery
 - Port scanning
 - Service detection
 - Version detection
 - Network reconnaissance
 - Security auditing
 - Identifying exposed services
 - Enumerating systems on a network
 - Vulnerability assessment preparation

---

## Industry usage for nmap
 - Penetration testing
 - Network administration
 - Security assessments
 - Infrastructure auditing
 - Attack surface analysis

---

all SS can be found in the Screenshots folder.