# OverTheWire Natas Walkthrough: Level 8 → Level 9

### Challenge Description
The goal of Level 8 is to find the correct secret value to submit to the form to unlock the password for Level 9.

* URL: http://natas8.natas.labs.overthewire.org
* Username: natas8
* Password: PSWD_HERE

---

## Walkthrough

### 1. Analyzing the Source Code
Navigate to the webpage and click the "View sourcecode" link. Looking inside the script, we see a hardcoded encoded string variable named encodedSecret and a custom function named encodeSecret which handles user input.

### 2. Identifying the Logic
The encodeSecret function processes user input through three nested steps from the inside out:
1. base64_encode converts the text to a Base64 string.
2. strrev takes that result and reverses the characters backward.
3. bin2hex takes the reversed text and converts it into a Hexadecimal string.

### 3. Reversing the Secret
Because these are simple encoding formats and not secure hashes, we can uncover the original secret by reversing the steps in the exact opposite order: Hex String to Hex Decode, to Reverse Text, to Base64 Decode.

You can do this directly in your linux terminal using the following single line pipeline:
echo "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d

### 4. Retrieving the Password
Running the terminal command returns the plaintext secret value. Take that decoded secret string, paste it back into the input field on the main Natas Level 8 webpage, and click Submit. The server will verify the secret and output your password for Natas Level 9.