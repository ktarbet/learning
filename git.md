https://bi-sdal.github.io/training/help-faq.html


## copy file from another repo with history
https://stackoverflow.com/questions/1365541/how-to-move-some-files-from-one-git-repo-to-another-not-a-clone-preserving-hi
```bash
cd repository
git log --pretty=email --patch-with-stat --reverse --full-index --binary -- path/to/file_or_folder > patch
cd ../another_repository
git am --committer-date-is-author-date < ../repository/patch 
```

## Cleanup
```bash
git reset --hard
git clean -fd
```


## create orphan branch to save some history 

```bash
git checkout --orphan archive-v3.0
rm -fr ./src/ ./test/ pom.xml build.gradle  build-DSSVue.xml 
rm -fr .git/index 
git remote add v30 ../hec-dssvue-v30/
git remote update
git merge --allow-unrelated-histories v30/master
git branch -l
git push -u origin archive-v3.0
```


## pushing just HEAD

git clone --depth 1 https://bitbucket.localhost/scm/dss/heclib.git   hec-heclib
git remote set-url origin  https://github.com/HydrologicEngineeringCenter/hec-heclib.git


-------

http://johnmathews.eu/rys-git-tutorial.html


https://www.youtube.com/watch?v=FyAAIHHClqI

#alias graph="git log --all --decorate --oneline --graph"


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
[karl@karl heclib]$ git remote set-url origin --add https://bitbucket.localhost/scm/dss/heclib.git
[karl@karl heclib]$ git remote -v show
origin	http://localhost:3000/ktarbet/heclib.git (fetch)
origin	http://localhost:3000/ktarbet/heclib.git (push)
origin	https://bitbucket.localhost/scm/dss/heclib.git (push)
```


## create branch from local edits

git checkout -b bug/ts_readv6

##  push that branch back to the server

git push -u origin bug/ts_readv6

# get back to original version of a file.
git reset headers/myheader.h

# get a file from another branch

```bash
https://stackoverflow.com/questions/10784523/how-do-i-merge-changes-to-a-single-file-rather-than-merging-commits/11593308#11593308
git checkout master  (working from master)
 git checkout --patch develop .vscode/launch.json   # launch.json exists in master
 git checkout  develop .vscode/launch.json          # launch.json does not exist in master.
```

## diff two branches

git diff master...bug/segfault


# rewrite history  deleting big files
#https://stackoverflow.com/questions/8083282/how-do-i-remove-a-big-file-wrongly-committed-in-git

https://stubbisms.wordpress.com/2009/07/10/git-script-to-show-largest-pack-objects-and-trim-your-waist-line/

https://rtyley.github.io/bfg-repo-cleaner/

java -jar /home/karl/Downloads/bfg-1.14.0.jar --no-blob-protection --delete-files '*.{db,sdf,dll}' /home/karl/project/heclib-archive

git reflog expire --expire=now --all && git gc --prune=now --aggressive


