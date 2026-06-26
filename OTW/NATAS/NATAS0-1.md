# OverTheWire Natas Walkthrough: Level 0 → Level 1

### Challenge Description
The goal of Level 0 - 1 is to find the password hidden somewhere on the landing page to gain access to Level 2. 

* **URL:** `http://natas1.natas.labs.overthewire.org`
* **Username:** `natas1`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas1:PSWD_HERE`. The webpage displays a single sentence:
> *"You can find the password for the next level on this page, but rightclicking has been blocked!"*
 On trying to right click an alert shows saying it has been blocked

### 2. Inspecting the Source Code
Because the password is not rendered visibly on the front-end interface, and right clicking is blocked we press
``` text
 f12
```
Allows to open developer console 

We can confirm that right clicking has been banned on this as there exists functions for them,

We then go through to the source code to find the comment with the answer 

### 3. Locating the Flag
Upon looking at the source code structure, you will find the flag explicitly written in a comment tag near the main text content:

```html
<html>
<head>
    <!-- You can find stylesheets or meta tags here -->
</head>
<body>
<h1>natas0</h1>
<div id="content">
You can find the password for the next level on this page.
<!-- The password for natas2 is PSWD_HERE -->
</div>
</body>
</html>