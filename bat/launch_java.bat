@echo off
setlocal enabledelayedexpansion

set count=1
for %%a in (%*) do (
    echo arg[!count!] = %%a
    set /a count+=1
)

endlocal
