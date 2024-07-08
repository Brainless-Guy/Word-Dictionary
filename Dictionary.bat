@echo off

REM Set the task name to check
set TaskName="Dictionary"
set root=%~dp0
REM Check if the task already exists
schtasks /query /tn %TaskName% > nul 2>&1
if %errorlevel% equ 0 (
    echo Task '%TaskName%' already exists.
) else (
    

    REM Create the scheduled task with highest privileges, hidden window, and run whether user is logged on or not
    schtasks /create /tn %TaskName% /tr %root%Dictionary.bat /sc daily  /IT

    echo Task '%TaskName%' created successfully to run on user login with highest privileges, hidden window, and run whether user is logged on or not.
)


pip3 install -r %root%requirements.txt

python3 %root%Word.py

pause
