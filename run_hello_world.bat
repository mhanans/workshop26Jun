@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv" (
    echo No virtual environment found. Run run.bat first to set things up.
    pause
    exit /b 1
)

call ".venv\Scripts\activate.bat"
python hello_world.py

pause
