# OverTheWire Natas Walkthrough: Level 4 → Level 5

### Challenge Description
The goal of Level 4 - 5 is to find the password hidden somewhere on the landing page to gain access to Level 6. 

* **URL:** `http://natas5.natas.labs.overthewire.org`
* **Username:** `natas5`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas5:PSWD_HERE`. The webpage displays the sentence:
> *"Access disallowed. You are not logged in"*

### 2. Checking the source code
The code did not reveal anything of importance, back to research
So get this, Websites determine if you are logged in using small data files called cookies or tokens stored in your browser
We try to find cookies, since they are to be stored, we check in memory first
Couldn't find it there ;-;
So we go to application tab and voila it is there
We find the following under cookies

```text
.
.
loggedin      0   ....
.
```

we change it to 1 >_< and then refresh

