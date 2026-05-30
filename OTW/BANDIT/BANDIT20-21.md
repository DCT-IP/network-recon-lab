# Bandit 20 -> 21
 - There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. 
 -It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). 
 -If the password is correct, it will transmit the password for the next level (bandit21).

## Commands
``` bash
 ls -l
 ./suconnect
  echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 2220 & sleep 1 && ./suconnect 2220
  echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 45678 & sleep 1 && ./suconnect 45678
```
## Observations and Mistakes
 - ./suconnect just like previous ones is a custom compiled setUID network client binary native 
 - nc was used to make sure the string in echo is passed via stdin
 - a random port worked and 2220 failed because, 2220 is actively bound(forgor :P)