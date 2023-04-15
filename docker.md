
## 

|Command | what is that ?|
| --- | --- |
| docker run -it -v -v$(pwd):/karl pydsstools /bin/bash|start up container with pwd mounted under /karl|
| docker run -it -v -v$(pwd):/karl:z pydsstools /bin/bash|same as above but with :z to work wtih SELinux permission|





```bash  
  116  docker ps -a
  117  docker stop --help
  118  docker stop web dblink
  119  docker ps
  120  docker ps --all
  121  docker run -it centos bash
  122  docker ps -a
  138  docker ps -l
  139  docker start 87752d85eca5
  140  docker attach 87752d85eca5
  142  docker ps -a
  143  docker run -it --name container-data -h CONTAINER -v /data debian /bin/bash
  146  docker run -it --name container-dataa -h ACONTAINER -v /data debian /bin/bash
  147  docker run -it -h NEWCONTAINER --volumes-from container-data debian bash
  148  docker run -it -h NEWCONTAINER2 --volumes-from container-data debian bash
  149  history
  ```
  
 ```bash
[root@vmhyd1 ~]# docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
docker.io/ubuntu              latest              113a43faa138        2 weeks ago         81.2 MB
docker.io/centos              latest              49f7960eb7e4        2 weeks ago         200 MB
docker.io/debian              latest              8626492fecd3        7 weeks ago         101 MB
docker.io/training/webapp     latest              6fae60ef3446        3 years ago         349 MB
docker.io/training/postgres   latest              6fa973bb3c26        4 years ago         365 MB
[root@vmhyd1 ~]# docker create -v /testdb2 --name testdb2 training/postgres /bin/true
6cf2ce579738f10124aeeef919fbbd4a2eedf99a9f0a2f69c26ad1c4c2ddba55

[root@vmhyd1 ~]# docker run --volumes-from testdb2 -v$(pwd):/backup ubuntu tar cvf /backup/testdb2.tar /testdb2

# add a file a.txt the commit to new image
[root@vmhyd1 ~]# docker run -it ubuntu bash
root@739f61ede881:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@739f61ede881:/# echo "hello"
hello
root@739f61ede881:/# echo "hello" >a.txt
root@739f61ede881:/# exit
exit
[root@vmhyd1 ~]# docker commit -m "add a.txt" \739  ktarbet/ubuntu:test
sha256:711d3d7836cc85e7b4e5faef04d15418834470dbd41c60d259af4fbf86589018
[root@vmhyd1 ~]# docker run -it ktarbet/ubuntu:test bash
root@9b30a93b16d4:/# cat a.txt
hello
root@9b30a93b16d4:/# exit
exit
```


## install docker-compose  Rocky Linux 8
ref: https://www.linuxtechi.com/install-docker-and-docker-compose-rocky-linux/

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
file /usr/local/bin/docker-compose 
```
