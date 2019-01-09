Find which Jar file ClassName is inside 
for /f "delims=" %f in ('dir /s /b "c:\CWMS 3.1\common\jar\*.jar"') do @echo %f & (c:\java\bin\jar -tf "%f" | findstr ClassName)

for /f "delims=" %f in ('dir /s /b "c:\project\heclib\jar\*.jar"') do @echo %f & (c:\java\bin\jar -tf "%f" | findstr ClassName)
