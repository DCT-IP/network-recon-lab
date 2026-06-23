# Bandit 25 -> 26
 - Logging in to bandit26 from bandit25 should be fairly easy… 
 -The shell for user bandit26 is not /bin/bash, but something else. 
 - Find out what it is, how it works and how to break out of it.

## Commands 
``` bash
 ls 
 cat /etc/passwd | grep bandit26
 cat bandit26.sshkey
 logout
 nano ~/bandit26.sshkey
 chmod 600 ~/bandit26.sshkey
 ssh -i ~/bandit26.sshkey -p 2220 bandit26@bandit.labs.overthewire.org
 :set shell=/bin/bash
 :shell
```