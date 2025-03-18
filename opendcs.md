Configuration Depot

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
gradlew runApp -Popendcs.app=dbedit -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.debug=5005

gradlew runApp -Popendcs.app=msgaccess -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.debug=5005

(karl) C:\project\opendcs>gradlew runApp -Popendcs.app=rs -Popendcs.profile="%appdata%\.opendcs\xml.profile" -Popendcs.arg=issue877
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
