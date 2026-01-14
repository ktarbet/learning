@echo off
setlocal enabledelayedexpansion

set REPORT_CSV=c:\tmp\monolith-study.csv
if exist %REPORT_CSV% del %REPORT_CSV%

:: DssVue
::call gradlew.bat run --args="--column dssvue --output-file=%REPORT_CSV% --reference-jar C:\bin\HEC-DSSVue-4.0.9\jar\hec-monolith-7.0.4.jar --filter hec-monolith --classpath C:\bin\HEC-DSSVue-4.0.9\jar\*;C:\bin\HEC-DSSVue-4.0.9\jar\ext\* C:\bin\HEC-DSSVue-4.0.9\jar\dssgui-4.0.9.jar C:\bin\HEC-DSSVue-4.0.9\jar\ext\*.jar"

:: MetVue

set MV_MODULES=C:\bin\HEC-MetVue-3.4.1\metvue\modules
set MV_JAR=%MV_MODULES%\ext\mil.army.usace.hec.metvue.MetVueJars
set MV_GUI=%MV_MODULES%\mil-army-usace-hec-metvue-MetVueGui.jar

set CP="%MV_JAR%\mil-army-usace-hec\*;%MV_JAR%\mil-army-usace-hec-map\hec-osmmap.jar;%MV_JAR%\mil-army-usace-hec-nf-framework\nf-framework-core.jar;%MV_JAR%\com-rma-paint\*;%MV_GUI%;%MV_MODULES%\*"

echo MetVue Classpath: %CP%
call gradlew.bat run --args="--column metvue --output-file=%REPORT_CSV% --reference-jar %MV_JAR%\mil-army-usace-hec\hec-monolith.jar --filter hec-monolith --classpath %CP%  %MV_GUI% %MV_MODULES%\*"

:: RTS

set CWMS_SHARED="C:\bin\CWMS-3.5.0\shared\jar"
set CWMS="C:\bin\CWMS-3.5.0\"

call gradlew.bat run --args="--column rts-app --output-file=%REPORT_CSV% --reference-jar %CWMS_SHARED%\hec-monolith-6.0.0-rc03.jar --filter hec-monolith --classpath %CWMS_SHARED%\*;%CWMS_SHARED%\ext\*;%CWMS_SHARED%\sys\*;%CWMS%\CAVI\jar\ext\*;%CWMS%\HEC-HMS\lib\hms-command-1.1.jar %CWMS_SHARED%\RTS-Application-3.5.0.jar %CWMS_SHARED%\*.jar"


::  FIA

set FIA_JAR=C:\bin\HEC-FIA-3.4.1\jar
call gradlew.bat run --args="--column fia --output-file=%REPORT_CSV% --reference-jar %FIA_JAR%\hec-monolith-4.0.1.jar --filter hec-monolith --classpath %FIA_JAR%\*;%FIA_JAR%\system\*  %FIA_JAR%\fia-nf-3.4.1.jar"



:: ResSim
set RESSIM_JAR="C:\bin\HEC-ResSim-4.0\jar"
call :create_classpath %RESSIM_JAR% "hec-*.jar" HEC
call :create_classpath %RESSIM_JAR% "dss*.jar" DSS
call :create_classpath %RESSIM_JAR% "cwms*.jar" CWMS
call :create_classpath %RESSIM_JAR% "ResSim*.jar" RSS
set CP=!HEC!;!DSS!;!CWMS!;!RSS!


call gradlew.bat run --args="--column ressim --output-file=%REPORT_CSV% --reference-jar %RESSIM_JAR%\hec-monolith-6.2.0.jar --filter hec-monolith --classpath %CP%  %RESSIM_JAR%\ResSimApp-4.0.1.jar"


:: OpenDCS
call gradlew.bat run --args="--column opendcs --output-file=%REPORT_CSV% --reference-jar C:\bin\opendcs-7.0.16-RC15\dep\hec-monolith-2.0.2.jar --filter hec-monolith --classpath C:\bin\opendcs-7.0.16-RC15\bin\opendcs.jar;C:\bin\opendcs-7.0.16-RC15\dep\* C:\bin\opendcs-7.0.16-RC15\bin\*.jar" 

:: HMS
call gradlew.bat run --args="--column hms --output-file=%REPORT_CSV% --reference-jar C:\bin\HEC-HMS-4.13\lib\hec-monolith-3.3.28.jar --filter hec-monolith --classpath C:\bin\HEC-HMS-4.13\lib\*;C:\bin\HEC-HMS-4.13\hms.jar C:\bin\HEC-HMS-4.13\hms.jar"


:: SSP
call :create_classpath "c:\bin\HEC-SSP-2.3.1-beta.1\lib" "hec-*.jar" CP
set CP=C:\bin\HEC-SSP-2.3.1-beta.1\lib\ssp.jar;!CP!

call gradlew.bat run --args="--column ssp --output-file=%REPORT_CSV% --reference-jar C:\bin\HEC-SSP-2.3.1-beta.1\lib\hec-monolith-3.3.23.jar --filter hec-monolith --classpath %CP% C:\bin\HEC-SSP-2.3.1-beta.1\lib\ssp.jar"




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