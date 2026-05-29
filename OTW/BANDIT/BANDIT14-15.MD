# Bandit 14 -> 15
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

## Commands
```bash
 nc localhost 30000
 <enter password>
``` 
OR
``` bash
 telnet localhost 30000
 <enter password>
 ^
```

## Observations
 - nc -> networking tool for scripting, piping and debugging
 - telnet -> emulation protocol, designed specifically for remote login

