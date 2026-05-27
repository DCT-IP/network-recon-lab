# Bandit 6 -> 7
 - Goal here to find password in the somewhere in the directory where
                                                    - owned by user bandit7
                                                    - owned by group bandit6
                                                    - 33 bytes in size

---

## Commands 
 - the following is the commands i put in order
``` bash
  find ./ type f -user bandit7 -group bandit6 -size 33c
  find / type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
  cd <dir>
  cat <filename>
  ```

---

## Observations and mistakes
- this time find operations had additional flags for user and group
- 2>/dev/null -> if Fd2(std err) then redirect(>) to /dev/null(discards al data written to it)
- initially i wrote ./, this causes it to search in the folder i am in (inclusive of subfolders), on changing to / would have allowed me to look everywhere but again cause a flood of errors to be shown. thus the expression 2>/dev/null