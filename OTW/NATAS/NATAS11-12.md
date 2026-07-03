================================================================================
# OverTheWire Natas Walkthrough: Level 11 → Level 12
================================================================================

## Challenge Description
The goal of Level 12 is to exploit an unrestricted file upload vulnerability to execute arbitrary PHP commands and read the password for Level 13.

* **URL:** http://natas12.natas.labs.overthewire.org
* **Username:** natas12

---

## Walkthrough

### 1. Analyzing the Interface
Upon logging in, we are presented with a simple file upload form meant for small image uploads (max 1KB).

### 2. Finding the Vulnerability
- Looking at the source code reveals that the application renames uploaded files to a random string to prevent overwriting.
- However, the script extracts the file extension from a client-side hidden input field in the HTML form: `<input type="hidden" name="filename" value="xxxx.jpg" />`.
- Because the extension is pulled from an input value that the user controls rather than the actual file metadata, the file extension validation can be entirely bypassed.

### 3. Exploiting the Vulnerability
- We create a tiny PHP web shell (`shell.php`) that executes system commands via query parameters.
- Using browser developer tools (F12), we inspect the upload form and manually change the hidden `filename` input value from `.jpg` to `.php`.
- We select our PHP script and submit the form. The server extracts the tampered `.php` extension, writes the file to the `upload/` directory, and provides a direct URL to it.
- Navigating to the uploaded script and appending `?cmd=cat /etc/natas_webpass/natas13` executes the system command and prints the flag.
================================================================================