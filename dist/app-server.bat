@echo off
SET ROOT_DIR=%~dp0


setlocal
cd %ROOT_DIR%


rem start
app-server\app-server.exe --open-browser apps

rem press enter to continue...
echo.
pause
