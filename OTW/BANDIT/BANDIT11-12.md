# Bandit 11 -> 12
 - The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
---
## Commands
``` bash
  ls
  cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
---
## Observations
 - since ROT13 cipher and other ROT ciphers are homomorphic in nature, so on attaching rot13 on encrypted data we can get the actual data back

---
