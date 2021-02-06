@echo off
SET ROOT_DIR=%~dp0..


setlocal
cd %ROOT_DIR%


rem build
pyinstaller app-server.spec

rem 💩 how to cp -r apps dist/ on windows
exit /b 1
