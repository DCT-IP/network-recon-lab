# Bandit 7 -> 8
 - The password is in the file data.txt, next to the word millionth

---

## Commands
``` bash
  find / type f -name data.txt | grep millionth
  find / type f -name data.txt 2>/dev/null | grep millionth
  ls 
  du data.txt
  cat data.txt | grep millionth
```

---

## Observations and Mistakes
 - intially the first two commands failed because find command does not open files.
 - on using du we find the size to be very big so opening it would cause problem.
 - to counter this we use pipes and search the line with the word required.

---