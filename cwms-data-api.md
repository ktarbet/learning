
Clean Ubuntu 22.04.3 LTS - under VMWare 


```bash
sudo apt install git
sudo snap install --classic code
sudo apt-get install openjdk-8-jdk
git clone https://github.com/USACE/cwms-data-api.git
```
edit /etc/hosts add the following line
127.0.0.1 cwms-data.localhost auth.localhost traefik.localhost

cd cwms-data-api/ompose_files/pki directory run `./genall.sh
# sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_version/bin/java
