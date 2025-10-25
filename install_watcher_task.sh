#!/bin/bash
echo "Installing Downloads Folder Watcher for Mac..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/watcher.py"
PLIST_NAME="com.downloadsorganizer.watcher"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"

# Create launchd plist
cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$PLIST_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>python</string>
        <string>$PYTHON_SCRIPT</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/downloads_watcher.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/downloads_watcher_error.log</string>
</dict>
</plist>
EOF

# Load the service
launchctl load "$PLIST_PATH"

echo ""
echo "Watcher installed successfully!"
echo "The watcher will run automatically when Mac starts."
echo ""
echo "To unload: launchctl unload $PLIST_PATH"
echo "To remove: rm $PLIST_PATH"
