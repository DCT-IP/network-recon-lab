# Bandit 13 -> 14
 - The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.

## Commands
``` bash
 ls -la
 logout
 scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
 ls 
 cp sshkey.private ~/sshkey.private
 cd ~
 chmod 600 sshkey.private
 ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
## Observations and mistakes
 - SCP's usage was taught
 - permissions' expressino in the form of numbers

