# Bandit 19 -> 20
 -To gain access to the next level, you should use the setuid binary in the homedirectory. 
 - Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Commands
``` bash
 ls -l
 ./bandit20-do
 ./bandit20-do whoami
 ls -l /etc/bandit_pass
 cat /etc/bandit_pass/bandit20
 ./bandit20-do whoami cat etc/bandit_pass/bandit20
```

## Observation
 - the s in the perms make it such that bandit20-do can be used by bandit19 too
 - on using it with cat <path/file> we opened the file to be opened only by bandit20 user 
