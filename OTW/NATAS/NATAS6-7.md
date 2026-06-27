# OverTheWire Natas Walkthrough: Level 6 → Level 7

### Challenge Description
The goal of Level 6 - 7 is to find the password hidden somewhere on the landing page to gain access to Level 8. 

* **URL:** `http://natas7.natas.labs.overthewire.org`
* **Username:** `natas7`
* **Password:** `answer in previous level`

---

## Walkthrough

### 1. Accessing the Page
Navigate to the URL provided and authenticate using the credentials `natas7:PSWD_HERE`.
The webpage has two links Home and About

### 2. Identifying the Vulnerability
When clicking the "Home" and "About" links, notice how the URL changes:
* Clicking **Home** results in: `index.php?page=home`
* Clicking **About** results in: `index.php?page=about`

The website uses a `page` parameter to dynamically fetch and display local files. This indicates a potential **Local File Inclusion (LFI)** vulnerability, where the application blindly trusts user input to locate server files.

### 3. Finding the Hint
Right-click on the webpage and select **View Page Source** (or press `Ctrl + U`). Scroll to the bottom of the source code to find a hidden HTML comment:

```html
<!-- hint: password for webpass8 is in /etc/natas_webpass/natas8 -->
```

### 4.Exploiting and Fetching password
we replace the page=about or page = home with page=/etc/natas_webpass/natas8
this loads the actual file we need