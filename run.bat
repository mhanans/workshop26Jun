@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo   Playwright Workshop Demo - Setup and Run
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo ERROR: Python was not found on PATH.
    echo Install Python 3.9+ from python.org and try again.
    pause
    exit /b 1
)

if not exist ".venv" (
    echo [1/4] Creating virtual environment...
    python -m venv .venv
) else (
    echo [1/4] Virtual environment already exists.
)

call ".venv\Scripts\activate.bat"

echo [2/4] Installing Python dependencies...
pip install -r requirements.txt --quiet

echo [3/4] Installing Playwright browser (Chromium)...
playwright install chromium

echo [4/4] Running tests...
echo Note: test_debug_me.py fails ON PURPOSE - it's for debugging practice.
echo.
pytest tests --headed --html=report.html --self-contained-html

echo.
echo Report saved to report.html - opening it now...
start "" "report.html"

echo.
echo Done. Press any key to close this window.
pause >nul
