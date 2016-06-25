echo off
setlocal enabledelayedexpansion
rem %1传入端口号
for /f "delims=  tokens=1" %%i in ('netstat -aon ^| findstr %1 ') do (
set a=%%i
goto js
)
:js
taskkill /f /pid "!a:~71,5!"
rem pause>nul