@echo off
title Investment Bot
cd /d "%~dp0"
mode con: cols=60 lines=20
echo Starting Telegram Invest-Bot...
python main.py
pause