Ubunutu 24.04

###  VMWare Tools
sudo apt install open-vm-tools-desktop

### install VSCode
apt-get update

# sudo apt install default-jre

# Java
sudo update-alternatives --config java
sudo apt-get install openjdk-11-jdk


### Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker $USER
# reboot....


--- Postgresql ---
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-client
#sudo apt-get -y install postgresql




