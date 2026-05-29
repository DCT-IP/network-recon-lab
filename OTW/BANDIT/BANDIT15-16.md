# BANDIT 15 -> 16
 - The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

## Commands
``` bash
 man openssl
 openssl s_client -connect localhost:30001
 <password>
```

## Observations
 - OpenSSL:- implements SSl and TSL protocols, starts with a handshake, makes a secure pipe and then goes into waiting state
