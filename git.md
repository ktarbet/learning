
## Remote Branches

### show remote branches

git branch -r

### checkout a remote branch

git checkout --track  origin/simplify/simplify_startup_scripts

### update list of branches

git remote update origin --prune


## grab file from another branch

git checkout master ./heclib/heclib_c_v6v7/heclib_c_v6v7.vcxproj 

 
## remember password

git config credential.helper store

## switch git host

```bash
karl@karl heclib]$ git remote set-url origin http://localhost:3000/ktarbet/heclib.git
[karl@karl heclib]$ git remote -v show
origin	http://localhost:3000/ktarbet/heclib.git (fetch)
origin	http://localhost:3000/ktarbet/heclib.git (push)
```

I want to keep the original repo synced, whenever I push.

```bash
[karl@karl heclib]$ git remote set-url origin --add https://bitbucket.hecdev.net/scm/dss/heclib.git
[karl@karl heclib]$ git remote -v show
origin	http://localhost:3000/ktarbet/heclib.git (fetch)
origin	http://localhost:3000/ktarbet/heclib.git (push)
origin	https://bitbucket.hecdev.net/scm/dss/heclib.git (push)
```


## create branch from local edits

git checkout -b bug/ts_readv6

##  push that branch back to the server

git push -u origin bug/ts_readv6

# get back to original version of a file.
git reset headers/myheader.h

## diff two branches

git diff master...bug/segfault

