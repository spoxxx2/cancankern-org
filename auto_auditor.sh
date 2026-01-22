#!/bin/bash
# Path to your phone's camera folder
WATCH_DIR="/sdcard/DCIM/Camera"

echo "--- CANCAN KERN AUTO-WATCH ACTIVE ---"
echo "Watching for bin photos in: $WATCH_DIR"

inotifywait -m -e create "$WATCH_DIR" | while read path action file; do
    if [[ "$file" == *.jpg ]] || [[ "$file" == *.png ]]; then
        echo "New photo detected: $file"
        # Run your high-performance C++ audit
        aud
    fi
done
