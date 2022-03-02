# Rocky Linux 8 developer tools

```bash
sudo dnf group list
sudo dnf groupinstall "Development Tools"

# vscode
https://code.visualstudio.com/docs/setup/linux

```

# switch java versions
sudo alternatives --config java




## run RHEL7 basic image
docker run -v /home/karl/project:/project -it --name test2 registry.access.redhat.com/ubi7

yum install "@X Window System"

subscription-manager register --username <username> --password <password> --auto-attach
In Redhat web page add subscription
  then 
  #subscription-manager attach
  
## installing lastest GCC for centos 7
modified from:
https://unix.stackexchange.com/questions/477360/centos-7-gcc-8-installation

```
yum install centos-release-scl
yum install devtoolset-8
scl enable devtoolset-8 -- bash

```

vi .bash_pofile

source /opt/rh/devtoolset-8/enable 

## upgrading git
yum install rh-git218


source /opt/rh/rh-git218/enable 
