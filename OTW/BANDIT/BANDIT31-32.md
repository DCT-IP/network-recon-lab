# Bandit 31 -> 32
 - There is a git repository at ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo via the port 2220. 
 - The password for the user bandit31-git is the same as for the user bandit31.

## Commands 
``` bash
  git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo 
  ls repo
  cat repo/README.md
  cd repo
  git branch -a
  git log
  git show <id>
  git tag
  git show secret
```