# OverTheWire Natas Walkthrough: Level 3 → Level 4

### Challenge Description
The goal of Level 3 - 4 is to find the password hidden somewhere on the landing page to gain access to Level 5. 

* **URL:** `http://natas4.natas.labs.overthewire.org`
* **Username:** `natas4`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas4:PSWD_HERE`. The webpage displays the sentence:
> *"Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"*

With a link to Refresh Page.

### 2. FInding the password
We Click the link,  the site refreshes changing the senene to
> *"Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/""*

On checking via developer tools we see the following
```text
 <div id="Content">
  .
  .
   <div id="viewsource>
    <a href="index.php">Refresh page</a>
   </div>
  .
.
```
The website knows the request is coming from user: natas4, we look up how does a site know this
it is due to *referrer* 
on more research, we find how to exploit it
``` bash
curl -u natas4:[level_4_password] --referer "http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/
```
is one of the ways to do this