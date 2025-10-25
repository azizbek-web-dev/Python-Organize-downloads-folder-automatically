@echo off
echo Installing Downloads Folder Watcher as Windows Task...

REM Get the current directory
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%watcher.py
set TASK_NAME=DownloadsFolderWatcher

REM Create the task (runs on system startup)
schtasks /create /tn "%TASK_NAME%" /tr "python \"%PYTHON_SCRIPT%\"" /sc onstart /rl highest /f

echo.
echo Task created successfully!
echo The watcher will run automatically when Windows starts.
echo.
echo To view tasks: schtasks /query /tn %TASK_NAME%
echo To delete task: schtasks /delete /tn %TASK_NAME% /f
pause
