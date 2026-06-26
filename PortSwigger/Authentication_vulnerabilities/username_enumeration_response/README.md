# Lab: Username enumeration via subtly different responses

## 1. Vulnerability Overview
* **Type:** Authentication / Information Disclosure
* **Flaw:** The application returns a microscopically different response length based on whether the input username is valid or invalid due to a subtle punctuation or string formatting variance.

## 2. Recon & Discovery (The Anomaly)
* **Baseline (Invalid User):** Returns a standard error message template yielding an exact, uniform response length (e.g., `3352` bytes).
* **Outlier (Valid User):** Triggers a distinct response size (e.g., `3351` or `3353` bytes) because of a subtle text or formatting discrepancy in the response payload.

## 3. Exploit Steps
1. Intercepted a login request (`POST /login`) in Burp Proxy and sent it to **Intruder**.
2. Set up a **Sniper** attack targeting the `username` parameter, keeping the password static. Loaded the candidate usernames list.
3. Executed the attack and sorted the results table by the **Length** column to isolate the single username displaying an anomalous byte size.
4. Hardcoded that specific valid username into the payload positions pane and shifted the payload markers to enclose the `password` parameter (`§password§`).
5. Loaded the candidate passwords list and launched the second attack phase.
6. Identified the correct password by tracking the row that returned an HTTP **`302 Found`** status code.

## 4. Credentials Discovered
* **Username:** argentina
* **Password:** jordan