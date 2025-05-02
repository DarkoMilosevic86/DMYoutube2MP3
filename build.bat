@echo off
setlocal enabledelayedexpansion

title DMYoutube2MP3 builder

echo Welcome to the DMYoutube2MP3 builder!
echo.
set VENV_DIR=.venv
set MAIN_SCRIPT=DMYoutube2MP3.py
set DIST_NAME=DM_Youtube2MP3
set FFMPEG_FILE=ffmpeg.exe

echo ----------------------------------------
echo [1] Checking virtual environment...
echo ----------------------------------------

if not exist %VENV_DIR% (
    python -m venv %VENV_DIR%
)

echo ----------------------------------------
echo [2] Activating environment and installing dependencies...
echo ----------------------------------------

call %VENV_DIR%\Scripts\activate.bat

python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo Warning: requirements.txt does not exists.
)

echo ----------------------------------------
echo [3] Building using PyInstaller...
echo ----------------------------------------

pyinstaller --noconfirm --noconsole --name %DIST_NAME% ^
 --add-data "%FFMPEG_FILE%;." --icon="res/DMYoutube2MP3.ico" ^
 --version-file="res/version_info.txt" ^
 %MAIN_SCRIPT%

echo ----------------------------------------
echo [4] Finished!
echo ----------------------------------------
call %VENV_DIR%\Scripts\deactivate.bat
pause
