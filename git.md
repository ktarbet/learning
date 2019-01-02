
test driving gitea [https://gitea.io/en-us/](https://gitea.io/en-us/)

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

