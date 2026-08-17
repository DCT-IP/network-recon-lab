# Lab: Broken Brute-Force Protection, IP Block

## 1. Vulnerability Overview

* **Type:** Authentication / Brute-Force Protection Bypass
* **Flaw:** The application uses an IP-based brute-force protection mechanism that can be bypassed due to flawed counter/reset logic. A successful login to another account causes the failed-login counter to reset, allowing repeated password attempts against the victim account without triggering the IP block.

## 2. Recon & Discovery (The Anomaly)

* **Baseline:** Repeated failed login attempts against `carlos` eventually trigger an IP block.
* **Known Valid Account:** The supplied credentials `wiener:peter` can be used to authenticate successfully.
* **Key Observation:** A successful login as `wiener` resets the failed-login counter associated with the attacker's IP.
* **Logic Flaw:** By alternating failed attempts against `carlos` with successful logins as `wiener`, the brute-force protection can effectively be reset between attempts.

## 3. Exploit Steps

1. Intercepted a login request (`POST /login`) in Burp Proxy and sent it to **Intruder**.
2. Confirmed that repeated incorrect passwords for `carlos` eventually caused the application to block the attacking IP.
3. Tested the supplied valid credentials `wiener:peter` and observed that a successful login resets the failed-attempt counter.
4. Constructed the attack sequence so that password attempts against `carlos` were interspersed with successful authentication attempts using `wiener:peter`.
5. Loaded the candidate password list for `carlos` and executed the attack.
6. Compared the responses for each candidate password, looking for the response indicating successful authentication rather than the normal failed-login response.
7. Identified the valid password for `carlos`.
8. Logged in using the discovered credentials and accessed the account page to complete the lab.

## 4. Credentials Discovered

* **Known Account:** `wiener:peter`
* **Victim Username:** `carlos`
* **Victim Password:** `<discovered from candidate list>`

## 5. Key Takeaway

The important weakness is not simply that the application has an IP block, but that the **state of the protection mechanism can be manipulated through authentication to another account**.

A brute-force defense should properly track failed attempts against the targeted account and should not allow authentication to an unrelated account to reset the protection state.
