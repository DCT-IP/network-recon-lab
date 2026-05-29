# bandit 16 -> 17
 - The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. 
 -First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. 
 -There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Commands
``` bash
 man openssl
 nmap -p 31000-32000 localhost
 man nmap
 nmap -p port1,port2,port3,.. -sV localhost
 <keyboard interrupt>
 nmap -p 31000-32000 -sV  localhost  
 openssl s_client -connect localhost:port -quiet
```

## observation
 - nmap -sV took a lot of time, it is due to its aggressive nature.
 - 