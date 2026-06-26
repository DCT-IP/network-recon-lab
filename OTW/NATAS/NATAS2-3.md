# OverTheWire Natas Walkthrough: Level 2 → Level 3

### Challenge Description
The goal of Level 2 - 3 is to find the password hidden somewhere on the landing page to gain access to Level 3. 

* **URL:** `http://natas3.natas.labs.overthewire.org`
* **Username:** `natas3`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas3:PSWD_HERE`. The webpage displays a single sentence:
> *"There is nothing on this page"*


### 2. Inspecting the Source Code
One right clicking to open source code, we find the following
..
.
```text
<h1>natas2</h1>
<div id="content">
::before
"there is nothing on this page"
<!--No more information leaks!! .. -->
::after
</div>
```
..
.
ON researching, we find about ROBOTS.txt
Google typically cannot find a directory on a website because it is blocked by the robots.txt file or lacks internal links that allow crawlers to discover it
so we add it to the site as /robots.txt
it gave us the dir which is blocked 
we add it get the password from txt file


