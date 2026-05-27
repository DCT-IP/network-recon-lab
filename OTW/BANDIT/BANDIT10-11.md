# Bandit 10 -> 11
 - The password for the next level is stored in the file data.txt, which contains base64 encoded data
---
## Commands
 - cat data.txt
 - cat data.txt | base64 -d 
----
## Observations and Mistakes
 - On using simply cat, it gave the encoded text
 - To decode we used ```bash
                        base64 -d ```
                        , allowed for decoding
---