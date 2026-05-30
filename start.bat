@echo off
chcp 65001 > nul

start "업무말투변환기 서버" "%~dp0backend\run_server.bat"

timeout /t 3 /nobreak > nul

start "" "%~dp0frontend\index.html"
