# Bandit 12 -> 13
 - The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. 
---
## Commands
``` bash
 xxd -r data.txt > data
 file data_new
 mv data_new data_new.gz
 gzip -d data_new.gz
 bzip2 -d data_new.bz2
 tar -xf data_new.tar
 cat data8
 ls -la
```
---
## observations and mistakes
 - This was a russian doll problem, made many many mistakes as was unable to keepup with the new files mainly because the terminal was filled with stuff
 - above is not in order, it just showcases what was used and what wasn't
---