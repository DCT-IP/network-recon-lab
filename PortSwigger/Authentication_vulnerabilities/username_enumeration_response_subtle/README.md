# Lab: Username enumeration via subtly different responses

## 1. Vulnerability Overview
* **Type:** Authentication / Information Disclosure
* **Flaw:** The application returns a microscopically different error string based on whether the input username is valid or invalid. While input reflection scrambles raw length sorting, the response payload itself leaks user validity via a subtle punctuation discrepancy.

## 2. Recon & Discovery (The Anomaly)
* **Baseline (Invalid User):** Returns a standard error message template yielding a uniform text pattern containing a trailing full stop (e.g., `Invalid username or password.`).
* **Outlier (Valid User):** Triggers a distinct text variant missing the trailing full stop (e.g., `Invalid username or password`), making it easy to identify when using precise string extraction or comparison.

## 3. Exploit Steps
1. Intercepted a login request (`POST /login`) in Burp Proxy and sent it to **Intruder**.
2. Set up a **Sniper** attack targeting the `username` parameter, keeping the password static. Loaded the candidate usernames list.
3. Configured **Grep - Extract** under the Intruder Settings tab to isolate the exact error message text string from the application UI.
4. Executed the attack and sorted the results table alphabetically by the custom **Grep - Extract column** to isolate the single username with the punctuation anomaly.
5. Hardcoded that specific valid username into the payload positions pane and shifted the payload markers to enclose the `password` parameter (`§password§`).
6. Loaded the candidate passwords list and launched the second attack phase.
7. Identified the correct password by tracking the row that returned an HTTP **`302 Found`** status code.

## 4. Credentials Discovered
* **Username:** [Discovered Outlier Payload]
* **Password:** [Successful 302 Redirect Payload]