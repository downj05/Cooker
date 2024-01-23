@echo off
setlocal enabledelayedexpansion

rem Variables
set python_version=3.11.0
set python_url=https://www.python.org/ftp/python/%python_version%/python-%python_version%-amd64.exe
set git_repo_url=https://github.com/downj05/Cooker/main.zip

rem Check if Python is already installed
where python > nul 2>&1
if %errorlevel% equ 0 (
    python --version
    echo Python is already installed.
    goto :run_install
) else (
    echo Python is not installed.
)

rem Download and install Python
echo Downloading Python %python_version%...
curl -LJO %python_url%
echo Installing Python %python_version%...
start /wait python-%python_version%-amd64.exe /quiet PrependPath=1

rem Check if Python installation was successful
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to install Python.
    goto :end
) else (
    echo Python installed successfully.
)

:run_install
rem Download the latest zip from the Git repo
echo Downloading the latest zip from the Git repo...
curl -LJO %git_repo_url%

rem Extract the zip file
echo Extracting the zip file...
powershell -command "Expand-Archive -Path main.zip -DestinationPath ."

rem Run the provided install.bat inside the extracted zip
echo Running install.bat...
cd cooker-main
call install.bat

:end
