# OverTheWire Natas Walkthrough: Level 0 → Level 1

### Challenge Description
The goal of Level 0 is to find the password hidden somewhere on the landing page to gain access to Level 1. 

* **URL:** `http://natas0.natas.labs.overthewire.org`
* **Username:** `natas0`
* **Password:** `natas0`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas0:natas0`. The webpage displays a single sentence:
> *"You can find the password for the next level on this page."*

### 2. Inspecting the Source Code
Because the password is not rendered visibly on the front-end interface, it is embedded within the underlying HTML source code, hidden from casual viewing via an HTML comment (`<!-- comment -->`).

You can view the source file using any of the following methods:
* **Keyboard Shortcut:** Press `Ctrl + U` (Windows/Linux) or `Cmd + Option + U` (macOS).
* **Context Menu:** Right-click anywhere on the empty space of the webpage and select **View Page Source**.
* **URL Prefix:** Prepend `view-source:` to the URL in your browser's address bar:
  `view-source:http://natas0.natas.labs.overthewire.org`

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
<!-- The password for natas1 is PSWD_HERE -->
</div>
</body>
</html>