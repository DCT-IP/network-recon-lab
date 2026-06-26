# OverTheWire Natas Walkthrough: Level 1 → Level 2

### Challenge Description
The goal of Level 1 - 2 is to find the password hidden somewhere on the landing page to gain access to Level 3. 

* **URL:** `http://natas2.natas.labs.overthewire.org`
* **Username:** `natas2`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas1:PSWD_HERE`. The webpage displays a single sentence:
> *"There is nothing on this page"*


### 2. Inspecting the Source Code
One right clicking to open source code, we find the following
..
.
<h1>natas2</h1>
<div id="content">
::before
"there is nothing on this page"
<img src="files/pixel.png">
::after
</div>
..
.
then we add /files at the end of the link which open another site
I first tried to open the image to find some data, could not find much
Then i clicked on a txt file in the same site
it gave a list of passwords with the password of next level highlighted.
