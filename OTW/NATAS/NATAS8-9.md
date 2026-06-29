# OverTheWire Natas Walkthrough: Level 9 → Level 10

## Challenge Description
The goal of Level 9 is to exploit a vulnerability in the search form to retrieve the password for Level 10.

* **URL:** http://natas9.natas.labs.overthewire.org
* **Username:** natas9

---

## Walkthrough

### 1. Analyzing the Interface
Upon logging in, we are presented with a simple search form that looks for words in a dictionary:

Find words containing: [________________] [Search]

Below the input, there is a link to view the Source Code. Clicking it reveals how our input is being handled on the backend.

### 2. Code Review & Vulnerability Analysis
The relevant portion of the PHP source code is as follows:

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}

#### The Flaw: Command Injection
The passthru() function executes a system command and passes the raw output directly back to the browser. 

The code takes our input ($key) and directly concatenates it into the shell command without any sanitization or filtering. The intended command structure is:
grep -i <our_input> dictionary.txt

Because the input is trusted blindly, we can manipulate the shell's execution flow using command separators like a semicolon (;).

---

### 3. Exploitation

OverTheWire stores the passwords for upcoming levels in /etc/natas_webpass/. We can construct a payload to break out of the grep command and read the Level 10 password file instead.

By inputting `; cat /etc/natas_webpass/natas10 #` into the search box, the backend executes the following command:

grep -i ; cat /etc/natas_webpass/natas10 # dictionary.txt

#### Payload Breakdown:
* ; (Semicolon): Ends the original grep command early.
* cat /etc/natas_webpass/natas10: Executes a secondary command to read the password file.
* # (Comment character): Comments out the trailing dictionary.txt, preventing shell syntax errors.

### 4. Result
Submitting this payload successfully forces the server to output the contents of the password file directly to the web page, revealing the password for Level 10.