# Bandit 9 -> 10
 - The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters
---
## Commands
```bash
 cat data.txt | grep '='
 grep -a "==" data.txt
 strings data.txt | grep "="
```
---
## Observations and Mistakes
 - first command line showed that the file was filled with binary file, so cat gave only corrupted data
 - second command worked, but it gave said corrupted entries aswell
 - third command uses strings, this allows only strings to be inputed
---