@echo off
echo Installing Downloads Folder Organizer as Windows Task...

REM Get the current directory
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%organize_downloads.py
set TASK_NAME=DownloadsFolderOrganizer

REM Create the task (runs daily at 9 AM)
schtasks /create /tn "%TASK_NAME%" /tr "python \"%PYTHON_SCRIPT%\"" /sc daily /st 09:00 /f

echo.
echo Task created successfully!
echo The organizer will run daily at 9:00 AM
echo.
echo To view tasks: schtasks /query /tn %TASK_NAME%
echo To delete task: schtasks /delete /tn %TASK_NAME% /f
pause
