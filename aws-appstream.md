Contents
 - Batch file to create virtual disk (VHDX)
 - powershell setup script that runs as appstream starts
 - AppBlock Definition
 - Fleet Settings


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

## powershell setup script that runs as appstream starts

  -  mounts virtual disk in appstream
  -  copy OpenDCS shortcuts to desktop
  -  copy shim for finding Java

```ps1
# This is a AppStream startup script for a custom AppBlock for OpenDCS 
# 
# This script mounts a virtual disk called cwms.vhdx to windows Drive W:
# 
# ref:  https://docs.aws.amazon.com/appstream2/latest/developerguide/create-setup-script.html

$MountDriveLetter = "W:"
$appBlock = "CWMSClient2"
$vhdx = "cwms.vhdx"
$desktop = "C:\Users\PhotonUser\Desktop"
$PathToVHD = "C:\AppStream\AppBlocks\"+$appBlock+"\"+$vhdx

Write-Host "PathToVHD: $PathToVHD"
Write-Host $desktop

$ScriptFolder = $($PSScriptRoot+"\")

@"
select vdisk file='$($PathToVHD)'
attach vdisk
rescan
select partition 1
remove all noerr
assign mount='$($MountDriveLetter)'
exit
"@  | Set-Content -Path "$($ScriptFolder)tmp.txt" -Encoding UTF8

Get-Content -Path "$($ScriptFolder)tmp.txt"

Write-Host "Execute: diskpart /s '$($ScriptFolder)tmp.txt'"
diskpart /s "$($ScriptFolder)tmp.txt"

Write-Host "setup shortcuts"

Copy-Item -Path "w:\OpenDCS-Toolkit.lnk" -Destination $desktop
Copy-Item -Path "w:\LRGS Status.lnk"     -Destination $desktop
Copy-Item -Path "w:\RefList Edit.lnk"    -Destination $desktop

# shim to launch java, using a directory already in the path 
Copy-Item -Path "W:\java.bat"  -Destination C:\Users\PhotonUser\AppData\Local\Microsoft\WindowsApps
```

java.bat - contents
```
w:\jre\bin\java %*%
```


## AppBlock Definition
replace 'bucket-name' with name of bucket that has permisions granted to appStream


|Name | Value |
|---|---|
|Block Name | CwmsClient2 |
|Virtal Disk | arn:aws:s3:::bucket-name/cwms.vhdx |
|Setup Script |arn:aws:s3:::bucket-name/setup.ps1|
|set script executable| C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|
|Setup executable arguments|-ExecutionPolicy Bypass -NonInteractive -File setup.ps1|
|execution duration seconds|60|


## Applications

|Name | Value |
|---|---|
|Application Name | OpenDCS-Windows |
|Display Name | OpenDCS |
|Associated app block | CwmsClient2 |
|Application icon Object | s3://bucket-name/tools.png  (copy below)|

![tools](https://github.com/ktarbet/learning/assets/4818531/71af8245-9108-43ff-8aeb-4edb73bf13bc)


## Fleet Settings
|Name | Value |
|---|---|
|Instance type|stream.standard.medium|
|Platform type|Microsoft Windows Server 2019 Base|
|Fleet type|Elastic|
|Disconnect timeout|15 Minutes|
|Idle Disconnect Timeout|15 Minutes|
|Stream view|Desktop|
|Maximum session duration|60 Minutes|

