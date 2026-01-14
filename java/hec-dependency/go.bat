setlocal enabledelayedexpansion
del c:\tmp\monolith-study.csv

:: DssVue
call gradlew.bat run --args="--column dssvue --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-DSSVue-4.0.9\jar\hec-monolith-7.0.4.jar --filter hec-monolith --classpath C:\bin\HEC-DSSVue-4.0.9\jar\*;C:\bin\HEC-DSSVue-4.0.9\jar\ext\* C:\bin\HEC-DSSVue-4.0.9\jar\dssgui-4.0.9.jar C:\bin\HEC-DSSVue-4.0.9\jar\ext\*.jar"

:: OpenDCS
call gradlew.bat run --args="--column opendcs --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\opendcs-7.0.16-RC15\dep\hec-monolith-2.0.2.jar --filter hec-monolith --classpath C:\bin\opendcs-7.0.16-RC15\bin\opendcs.jar;C:\bin\opendcs-7.0.16-RC15\dep\* C:\bin\opendcs-7.0.16-RC15\bin\*.jar" 

:: HMS
call gradlew.bat run --args="--column hms --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-HMS-4.13\lib\hec-monolith-3.3.28.jar --filter hec-monolith --classpath C:\bin\HEC-HMS-4.13\lib\*;C:\bin\HEC-HMS-4.13\hms.jar C:\bin\HEC-HMS-4.13\hms.jar"


:: SSP
call :create_classpath "c:\bin\HEC-SSP-2.3.1-beta.1\lib" "hec-*.jar" CP
set CP=C:\bin\HEC-SSP-2.3.1-beta.1\lib\ssp.jar;!CP!
echo !CP!

call gradlew.bat run --args="--column ssp --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-SSP-2.3.1-beta.1\lib\hec-monolith-3.3.23.jar --filter hec-monolith --classpath %CP% C:\bin\HEC-SSP-2.3.1-beta.1\lib\ssp.jar"


:: ResSim
call :create_classpath "C:\bin\HEC-ResSim-4.0\jar" "hec-*.jar" CP

:: "C:\bin\HEC-ResSim-4.0\jar\ResSimApp-4.0.1.jar"
::call gradlew.bat run --args="--column ressim --output-file=c:\tmp\monolith-study.csv --reference-jar C:\bin\HEC-ResSim-4.0\jar\hec-monolith-4.0.1.jar --filter hec-monolith --classpath C:\bin\HEC-ResSim-4.0\jar\* C:\bin\HEC-ResSim-4.0\jar\ResSimApp-4.0.1.jar"


:: RTS


goto :eof

:create_classpath
:: %1 is the first argument (directory)
:: %2 is the second argument (filter)
:: %3 is the third argument (the name of the variable to store the output)

set "CP_DIR=%~1"
set "FILTER=%~2"
set "RETURN_VAR=%~3"

set "CP="

:: Loop through all files matching the filter and append them
for %%f in ("%CP_DIR%\%FILTER%") do (
    set "CP=!CP!;%%f"
)

:: Set the return variable (using the name passed in %3) to the final classpath value
set "%RETURN_VAR%=%CP%"

:: Return from the subroutine
goto :eof