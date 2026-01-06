
del c:\tmp\monolith-study.csv

call gradlew.bat run --args="--column opendcs --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\opendcs-7.0.16-RC15\dep\hec-monolith-2.0.2.jar --filter hec-monolith --classpath C:\bin\opendcs-7.0.16-RC15\bin\opendcs.jar;C:\bin\opendcs-7.0.16-RC15\dep\* C:\bin\opendcs-7.0.16-RC15\bin\*.jar" 

call gradlew.bat run --args="--column hms --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-HMS-4.13\lib\hec-monolith-3.3.28.jar --filter hec-monolith --classpath C:\bin\HEC-HMS-4.13\lib\*;C:\bin\HEC-HMS-4.13\hms.jar C:\bin\HEC-HMS-4.13\hms.jar"

call gradlew.bat run --args="--column dssvue --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-DSSVue-4.0.9\jar\hec-monolith-7.0.4.jar --filter hec-monolith --classpath C:\bin\HEC-DSSVue-4.0.9\jar\*;C:\bin\HEC-DSSVue-4.0.9\jar\ext\* C:\bin\HEC-DSSVue-4.0.9\jar\dssgui-4.0.9.jar C:\bin\HEC-DSSVue-4.0.9\jar\ext\*"

