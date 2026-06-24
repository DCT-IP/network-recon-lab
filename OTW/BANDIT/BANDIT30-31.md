# Bandit 29 -> 30
 - There is a git repository at ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo via the port 2220. 
 -The password for the user bandit29-git is the same as for the user bandit29..

## Commands 
``` bash
  git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo 
  ls repo
  cat repo/README.md
  cd repo
  git branch -a
  git log
  git show <id>
  git tag
  git show secret
```