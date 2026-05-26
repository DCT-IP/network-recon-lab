# Bandit 5 - 6
 - Goal here to find password in the inhere directory where
                                                    - it is in human readable format
                                                    - 1033 bytes in size
                                                    - not executable
---
## Commands
> ls -a
>
> find ./inhere -type f -size 1033c ! -executable -readable -exec file {} \; | grep ASCII;
>
>cd <dir>
>
>cat "filename"

---
## Problems
 - had to look up stackoverflow for the expression to find the not executables
 - I had before hand went into /inhere, to be able to use the copied i had to go to cd ..(prev dir)
 -Better was to do was to write 
 ```bash
    find ./ -type f -size 1033c ! -executable -readable -exec file {} \; | grep ASCII
 ```

---
