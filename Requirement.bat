@echo off
echo Checking Python installation...

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Checking pip installation...
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed or not in PATH
    pause
    exit /b 1
)

echo Installing Python requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements
    pause
    exit /b 1
)

echo Requirements installed successfully!
pause