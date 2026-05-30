# Bandit 18 -> 19
 - The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Commands
``` bash
 ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

## Observations and mistakes
 - last level's syntax was mixed up
 - u can send commands u want to perform wit ssh in double quotes