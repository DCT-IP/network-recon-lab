# Bandit 17 -> 18
 - There are 2 files in the homedirectory: passwords.old and passwords.new. 
 - The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

## Commands
 - Began by making the file for the ssh the RSA key file
``` bash
 ls
 grep -xvFf passwords.old passwords.new
```

## Observations
 - -x matches the entire line
 - -v inverts it i.e. those who don't mtch
 - -F treats patterns as fixed strings
 - -f reads patterns from passwords.new
