# Bandit 29 -> 30
 - There is a git repository at ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo via the port 2220. 
 -The password for the user bandit29-git is the same as for the user bandit29..

## Commands 
``` bash
  git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo 
  ls repo
  cd repo
  cat README.md
  git branch -a
  git checkout dev
  cat README.md
```