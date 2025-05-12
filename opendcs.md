#  OpenDCS  with CWMS-Oracle


To setup OpenDCS with CWMS-Oracle (For Developement/Testing) use the following steps:

1. Configure an OpenDCS property file for CWMS-Oracle.  "C:\Users\karl\AppData\Roaming\.opendcs\user.properties"
2. Configure OpenDCS username/password using the setDecodesUser OpenDCS program.
3. Start up a new Oracle instance that includes the CWMS schema.
4. Setup Oracle Permissions 
5. Install the OpenDCS (CCP) Schema using the manageDatabase OpenDCS program.

note: in this example I'm using windows client and Oracle under Docker (on Linux)


##  configure a OpenDCS property file for CWMS-Oracle

```text
EditDatabaseType=CWMS
EditDatabaseLocation=jdbc\:oracle\:thin\:@127.0.0.1\:1521/FREEPDB1?oracle.net.disableOob=true
EditPresentationGroup=SHEF-English
SiteNameTypePreference=cwms
EditTimeZone=UTC
EditOutputFormat=Human-Readable
jdbcDriverClass=oracle.jdbc.driver.OracleDriver
SqlKeyGenerator=decodes.sql.OracleSequenceKeyGenerator
transportMediumTypePreference=goes
dataTypeStdPreference=CWMS
dbAuthFile=C\:/Users/karl/AppData/Roaming/.opendcs/oracle-test.auth
dbOfficeId=NWDM
CwmsOfficeId=NWDM

```

## configure OpenDCS username/password using setDecodesUser OpenDCS program

```bat
C:\project\opendcs\install\build\install\opendcs\bin>setDecodesUser %appdata%\.opendcs\oracle-test.auth    
Creating or Updating: C:\Users\karl\AppData\Roaming\.opendcs\oracle-test.auth
Please enter a username: S0HECTEST
Please provide a password:test
Please repeat the password:test
```


## Start up a new Oracle instance that includes the CWMS schema.

note: the docker command below creates several users are created including:S0HECTEST, S0CWMSPD,...

we will be using S0HECTEST as the 'regular' OpenDCS user

```bash

docker run  --rm -d -p 1521:1521 --name opendcs-oracle \
        -e ORACLE_PASSWORD="test"  \
        -e CWMS_PASSWORD="test" \
        -e OFFICE_ID="HQ" \
        -e OFFICE_EROC="s0" \
        registry-public.hecdev.net/cwms/database-ready-ora-23.5:latest-dev
```

## Setup Oracle Permissions 

```sql
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Mgr','HQ');
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Proc','HQ');

EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Mgr','NWDM');
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Proc','NWDM');


EXEC cwms_sec.add_user_to_group('karl', 'CWMS Users','NWK');

exec CWMS_ccp_vpd.set_ccp_session_ctx(null, null, 'NWDM');

```

###  install the opendcs schema into Oracle

```
C:\project\opendcs\install\build\install\opendcs\bin>manageDatabase -I CWMS-Oracle 
Migrating Database:
Please enter the schema owning username and password for database at jdbc:oracle:thin:@oracledb:1521:FREEPDB1?oracle.net.disableOob=true,
username:S0HECTEST
password:
Please provide values for each of the presented properties.
CWMS_SCHEMA (desc = Name of the CWMS Schema to reference) = CWMS_20
CCP_SCHEMA (desc = Name of CCP schema to create.) = CCP
DEFAULT_OFFICE_CODE (desc = Integer value of the default office to assign) = 1
DEFAULT_OFFICE (desc = Ascii value of the default office to assign) = HQ
TABLE_SPACE_SPEC (desc = Name of table space, leave blank if you don't need a separate table space) = 
```

 ## Connect to Oracle

```
# sh-4.4$ sqlplus CWMS_20/test@localhost:1521/FREEPDB1?oracle.net.disableOob=true
```





## Example commands

```bash

dbedit -P "%appata%\.opendcs\nwdm-xml.properties"

```


## Configuration Depot

https://www.usgs.gov/apps/telemetry/index.html


https://www.usgs.gov/apps/telemetry/api/site?siteNumber=07137500


https://www.noaasis.noaa.gov/GOES/GOES_DCS/gdcs_pf.html

https://github.com/opendcs/opendcs




```bat
 C:\project\opendcs>gradlew spotbugsMain --info

 reports at:
 ./opendcs/java/opendcs/build/reports/spotbugs/main/spotbugs.html#{%22tab%22:%22listByCategories%22,%22includeFixed%22:false,%22release%22:-1,%22priority%22:4}
 ```

debugging with vscode.

```cmd

# run the launcher app
gradlew run

gradlew runApp -Popendcs.app=dbedit -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.debug=5005 -Pno.docs=true

gradlew runApp -Popendcs.app=msgaccess -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.debug=5005 -Pno.docs=true

gradlew runApp -Popendcs.app=rs -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.arg=issue877 -Pno.docs=true

gradlew runApp -Popendcs.app=dbimport -Popendcs.profile="%appdata%\.opendcs\NWK.profile" -Popendcs.debug=5005 -Pno.docs=true -Popendcs.arg="C:\tmp\dbexport-drsd.xml"
```


debug.settings
```json
{
    "version": "0.2.0",
    "configurations": [
    {
    "type": "java",
    "name": "Attach",
    "request": "attach",
    "hostName": "localhost",
    "port": 5005
    },
    ]
}
```


# Server Setup - Installing OpenDCS with Postgresql on Linux 

## Install PostgreSQL

```bash
docker run --name opendcs-pg -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres:16.2
```


###  configure user/password for using opendcs

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

unzip opendcs zip file.

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
./bin/manageDatabase -I OpenDCS-Postgres -P /home/hec/opendcs-install/decodes.properties
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


