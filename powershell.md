Powershell works on Windows, Mac, and Linux
 
get-module -list

get-service | where {$_.status -eq "Stopped"}

get-physicaldisk 


get-executionpolicy -Scope CurrentUser
