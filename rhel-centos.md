## for centos 7
modified from:
https://unix.stackexchange.com/questions/477360/centos-7-gcc-8-installation

```
yum install centos-release-scl
yum install devtoolset-8
scl enable devtoolset-8 -- bash

```

vi .bash_pofile

source /opt/rh/devtoolset-8/enable 

