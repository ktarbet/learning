
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


https://docs.docker.com/engine/install/ubuntu/
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

```bash
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-compose

```

sudo usermod -aG docker karl
docker-compose --env-file ../cda.env  up -d

https://localhost:8444/cwms-data/swagger-ui.html

docker-compose logs  data-api





