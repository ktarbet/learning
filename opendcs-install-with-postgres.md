
# Server Setup - Installing OpenDCS with Postgresql on Linux 

## Install PostgreSQL

```bash
docker run --name opendcs-pg -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres:16.2
```
ref: https://hub.docker.com/_/postgres

## Connect to PostgreSQL and create opendcs database that is owned by the  hydromet user

```bash
docker exec -it opendcs-pg /bin/bash

psql -U postgres

create role hydromet with createdb createrole  password 'x';
ALTER USER hydromet WITH LOGIN;
create database opendcs owner hydromet;
\q
```

## Install OpenDCS

java -jar /home/hec/opendcs/stage/opendcs-installer-7.0.12-RC04.jar

## Configure decodes.properties

vi opendcs/decodes.properties
```text
editDatabaseType:OPENTSDB
EditDatabaseLocation=jdbc:postgresql://localhost/opendcs
DbAuthFile=UserAuthFile:$HOME/.opendcs/.decodes.auth
```
set password for openDCS software tools

```bash
mkdir $HOME/.opendcs
./bin/setDecodesUser $HOME/.opendcs/.decodes.auth
User Name: hydromet
Password:
writing...
```


## Configure OpenDCS database

```text
./bin/migrateApp -I OpenDCS-Postgres -P /home/hec/opendcs-install/decodes.properties
Migrating Database:
username:hydromet
password:
Using jdbc URL: jdbc:postgresql://localhost/opendcs
Installing fresh database
Please provide values for each of the presented properties.
NUM_TS_TABLES (desc = How many tables should be used to partition numeric timeseries data.) = 1
NUM_TEXT_TABLES (desc = How many tables should be used to balance text timeseries data.) = 1
Please provided an admin user:admin
Please provide a password:admin
Please repeat the password:admin
```

Import required meta-data

```bash
./bin/dbimport ./edit-db/loading-app/*.xml
./bin/dbimport ./edit-db/enum/*.xml 
./bin/dbimport ./edit-db/eu/EngineeringUnitList.xml 
./bin/dbimport ./edit-db/datatype/DataTypeEquivalenceList.xml 
./bin/dbimport ./edit-db/presentation/*.xml 
./bin/compimport ./imports/comp-standard/*.xml

```





# Windows Client Install

java -jar C:\project\opendcs\stage\opendcs-installer-7.0.12-RC04.jar

note: This example istalled to C:\test\OPENDCS7.0.12-RC04

mkdir %USERPROFILE%\.opendcs
C:\test\OPENDCS7.0.12-RC04\bin>setDecodesUser.bat %USERPROFILE%\.opendcs\.decodes.auth
User Name: hydromet
Password:
writing...



