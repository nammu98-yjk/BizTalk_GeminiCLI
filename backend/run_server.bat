@echo off
chcp 65001 > nul
title 업무말투변환기 서버
cd /d "%~dp0"
C:\Users\82103\AppData\Local\Python\pythoncore-3.14-64\Scripts\uvicorn.exe main:app --reload --port 8000
pause
