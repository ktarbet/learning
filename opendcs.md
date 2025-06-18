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
dbAuthFile=C\:/Users/karl/AppData/Roaming/.opendcs/karl.auth
dbOfficeId=NWDM
CwmsOfficeId=NWDM

```

## configure OpenDCS username/password using setDecodesUser OpenDCS program

```bat
C:\project\opendcs\install\build\install\opendcs\bin>setDecodesUser %appdata%\.opendcs\oracle-test.auth    
Creating or Updating: C:\Users\karl\AppData\Roaming\.opendcs\karl.auth
Please enter a username: karl
Please provide a password:test
Please repeat the password:test
```


## Start up a new Oracle instance that includes the CWMS schema.

note: the docker command below creates several users/roles


|user      | password|
|----------|------|
| builduser| ?    |
| sys      | test |
| system   | test |
| s0hectest| ?    |


```bash
# docker pull ghcr.io/hydrologicengineeringcenter/cwms-database/cwms/database-ready-ora-23.5:latest-dev
docker stop opendcs-oracle
sleep 2
docker run  --rm -d -p 1521:1521 --name opendcs-oracle \
        -e ORACLE_PASSWORD="test"  \
        -e CWMS_PASSWORD="test" \
        -e OFFICE_ID="HQ" \
        -e OFFICE_EROC="s0" \
        ghcr.io/hydrologicengineeringcenter/cwms-database/cwms/database-ready-ora-23.5:latest-dev

sleep 1
docker logs -f opendcs-oracle
```


###  Install the opendcs schema into Oracle

```bat
manageDatabase  -d 3 -P "%appdata%\.opendcs\nwdm-test.profile" -username builduser -password test -appUsername karl -appPassword test -I CWMS-Oracle -DCWMS_SCHEMA=CWMS_20 -DCCP_SCHEMA=CCP -DDEFAULT_OFFICE_CODE=1  -DDEFAULT_OFFICE=HQ

```

```bat
Migrating Database:
Please provide values for each of the presented properties.
TABLE_SPACE_SPEC (desc = If data will be on a separate table space indicate the line here.) =
Installing fresh database
A default admin username will be created to allow initial data import and GUI configuration.
Now loading baseline data.
May 16, 2025 7:59:28 AM usace.cwms.db.jooq.AbstractCwmsDbDao testCompatibility_aroundBody0
WARNING: JOOQ CWMSDB API implemented for CWMS database schema version 18.1.21, connecting to version 99.99.99
Base line data has been imported. You may now begin using the software.
If you will be running background apps such as CompProc and the RoutingScheduler,
you should create a separate user. This is not currently covered in this application.
```


setup user karl to have permissions in two offices.
```sql 
EXEC cwms_sec.add_user_to_group('karl', 'CWMS Users','NWK');
EXEC cwms_sec.add_user_to_group('karl', 'CCP Mgr','NWK');
EXEC cwms_sec.add_user_to_group('karl', 'CCP Proc','NWK');

EXEC cwms_sec.add_user_to_group('karl', 'CWMS Users','NWDM');
EXEC cwms_sec.add_user_to_group('karl', 'CCP Mgr','NWDM');
EXEC cwms_sec.add_user_to_group('karl', 'CCP Proc','NWDM');

```


Now we can run programs such as dbedit and dbimport like this:

```bat
dbedit  -lCON  -d3  -P "%appdata%\.opendcs\nwk-test.profile"
```

```bat
dbimport  -lCON -d3  -P "%appdata%\.opendcs\nwk-test.profile" "C:\project\opendcs.support\import-issue\dbexport-drsd.xml"

```



----------------------------
# Other CWMS Oracle commands that may be helpful

```sql
-- the following for debugging/research
ALTER USER ccp
  GRANT CONNECT THROUGH builduser;


exec cwms_20.CWMS_ENV.SET_SESSION_OFFICE_ID ('NWK');

EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Mgr','HQ');
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Proc','HQ');
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Mgr','NWDM');
EXEC cwms_sec.add_user_to_group('S0HECTEST', 'CCP Proc','NWDM');
EXEC cwms_sec.add_user_to_group('karl', 'CWMS Users','NWK');
exec CWMS_ccp_vpd.set_ccp_session_ctx(null, null, 'NWDM');


-- checking vpd config for PLATFORMCONFIG (I get 4 rows on system where vpd is configured)
SELECT * FROM v$vpd_policy
WHERE object_owner = 'CCP'
AND object_name IN ('PLATFORMCONFIG');


SELECT SYS_CONTEXT('CWMS_ENV', 'SESSION_OFFICE_CODE') FROM DUAL

```


 ## Connect to Oracle

```
# sh-4.4$ sqlplus CWMS_20/test@localhost:1521/FREEPDB1?oracle.net.disableOob=true
```





## Example commands

```bash

dbedit -P "%appata%\.opendcs\nwdm-xml.properties"

dbimport -P %appdata%\.opendcs\nwdm-test.profile -v -l CON "C:\project\opendcs.support\import-issue\nwdm-all.xml"
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


