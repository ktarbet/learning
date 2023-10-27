Contents
 - Batch file to create virtual disk (VHDX)
 - powershell setup script that runs as appstream starts
     -  mounts virtual disk in appstream
     -  copy OpenDCS shortcuts to desktop
     -  copy shim for finding Java




## Batch file to create virtual disk (VHDX) 


```bat
:: Create Windows virtual disk with OpenDCS and Java installed
::
:: Requirements:
::   - opendcs-ot-7.0.*.jar in current directory
::   - jre directory in current directory 
::        Tested using https://adoptium.net/temurin/releases/?version=8&arch=x64&package=jre&os=windows

cd %~dp0
set VDISK=%CD%\cwms.vhdx

echo create vdisk file=%VDISK% maximum=4000 type=expandable >tmp{010}.txt
echo select vdisk file=%VDISK% >>tmp{010}.txt
echo attach vdisk >>tmp{010}.txt
echo convert mbr >>tmp{010}.txt
echo create partition primary >>tmp{010}.txt
echo format fs=ntfs quick >>tmp{010}.txt
echo assign Letter=W >>tmp{010}.txt
::echo assign mount=c:\apps\cwms >>tmp{010}.txt

diskpart /s tmp{010}.txt


jre\bin\java -jar opendcs-ot-7.0.8.jar opendcs-cfg.xml
xcopy jre W:\jre /E /I /H /Y

:: copy custom decodes.properties
copy decodes.properties w:\opendcs /Y

:: copy shortcuts
copy  %USERPROFILE%\Desktop\OpenDCS-Toolkit.lnk w:\
copy  "%USERPROFILE%\Desktop\LRGS Status.lnk" w:\
copy  "%USERPROFILE%\Desktop\RefList Edit.lnk" w:\
copy java.bat w:\

:: Un-mount VHDX

echo select vdisk file=%VDISK% >tmp{010}.txt
echo detach vdisk >>tmp{010}.txt
diskpart /s tmp{010}.txt

```

##powershell setup script that runs as appstream starts



