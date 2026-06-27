# OverTheWire Natas Walkthrough: Level 5 → Level 6

### Challenge Description
The goal of Level 5 - 6 is to find the password hidden somewhere on the landing page to gain access to Level 7. 

* **URL:** `http://natas6.natas.labs.overthewire.org`
* **Username:** `natas6`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas6:PSWD_HERE`. The webpage displays the sentence:
> *"Input Secret: <inputhere>"*
with a submit button and an option to view the source code.

### 2.How do we find the password
We go to source code, where we see the inner workings of it
here we find include `link`
so we redirect ourselves to the said link and we get our key

