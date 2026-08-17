# PortSwigger — Authentication Vulnerabilities

Notes and solutions from the **Authentication vulnerabilities** learning path on PortSwigger Web Security Academy.

This directory contains my personal notes while working through the labs, focusing on understanding **why each vulnerability exists, how to identify it, and how the exploit works** rather than simply recording payloads.

---

## Topics

The Authentication vulnerabilities section covers concepts such as:

- Authentication mechanisms
- Username enumeration
- Brute-force attacks
- Account lockout weaknesses
- Credential stuffing
- Authentication logic flaws
- Multi-factor authentication vulnerabilities
- Password reset vulnerabilities
- Other weaknesses in authentication flows

---

## Learning Approach

For each lab, the goal is to document:

1. **Vulnerability**
   - What is fundamentally wrong?

2. **Observation**
   - What behavior in the application reveals the vulnerability?

3. **Attack Logic**
   - How can the weakness be turned into an exploit?

4. **Exploit**
   - Relevant requests, payloads, or Burp Suite workflow.

5. **Why It Works**
   - The underlying application/security logic responsible for the vulnerability.

6. **Takeaway**
   - What defensive lesson or generalizable technique does the lab demonstrate?

The emphasis is on understanding the **reasoning behind the exploit**, not memorizing individual payloads.

---

## Tools

Primary tools used:

- Burp Suite
- Browser Developer Tools
- HTTP requests/responses
- Python or shell utilities when useful

---

## Notes

These are personal learning notes from working through PortSwigger Web Security Academy.

The objective is to build practical understanding that can later be transferred to real-world web application security assessments.