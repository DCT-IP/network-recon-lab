# Bandit 8 -> 9
 - the password is in data.txt and is only line of text that occurs only once

---

## Commands
``` bash
 cat data.txt | uniq -u
 sort data.txt | uniq - u
```

---

## Observations and Mistakes
 - the cat one gave many lines of text, this is because uniq compares with the prev one only. ie 
> If given apple, banana, apple, cherry, it will compare banana and cherry with apple only.
 - thus we sorted it, as shown in example
> It becomes apple, apple, banana, cherry, so it looks at apple and then apple again and removes it. 

---