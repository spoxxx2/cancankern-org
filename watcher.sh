#!/bin/bash
# CANCAN AUTOMATION WATCHER
# Monitors for new JPG/PNG files and triggers the Golden Overlord

echo "--- WATCHER ACTIVE: MONITORING 1501 PEARL ST ---"

inotifywait -m -e close_write --format '%f' . | while read FILENAME
do
    if [[ "$FILENAME" =~ \.(jpg|jpeg|png)$ ]]; then
        echo "NEW ASSET DETECTED: $FILENAME"
        echo "INITIATING C++ AUDIT..."
        ./super-aud
        echo "VAULT UPDATED & DEPLOYED."
    fi
done
