#!/bin/bash
echo "Installing Downloads Folder Organizer as Cron Job..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/organize_downloads.py"

# Make Python script executable
chmod +x "$PYTHON_SCRIPT"

# Add cron job to run daily at 9 AM
(crontab -l 2>/dev/null; echo "0 9 * * * cd '$SCRIPT_DIR' && python '$PYTHON_SCRIPT' >> /tmp/downloads_organizer.log 2>&1") | crontab -

echo ""
echo "Task created successfully!"
echo "The organizer will run daily at 9:00 AM"
echo ""
echo "To view cron jobs: crontab -l"
echo "To delete cron job: crontab -e"
