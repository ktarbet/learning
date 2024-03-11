

My Basic Ubunutu  setup

install VSCode

sudo apt install default-jre

sudo apt-get install openjdk-8-jdk

apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-compose


sudo update-alternatives --config java

sudo usermod -aG docker $USER

sudo usermod -aG sudo $USER


--- Postgresql ---
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-client
#sudo apt-get -y install postgresql




