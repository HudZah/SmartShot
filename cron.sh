#!/bin/bash

FOLDER="$HOME/Documents/Screenshots"
LAST_FILE="$HOME/.last_screenshot_check"

# Get the most recent file
NEWEST_FILE=$(find "$FOLDER" -type f -print0 | xargs -0 ls -t | head -1)

# Compare with the last check
if [ "$NEWEST_FILE" != "$(cat "$LAST_FILE" 2>/dev/null)" ]; then
    echo "$NEWEST_FILE" > "$LAST_FILE"
    /usr/bin/python3 /path/to/your/script.py
fi
