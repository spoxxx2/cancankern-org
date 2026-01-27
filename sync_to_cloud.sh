#!/bin/bash
# 1. Create a timestamped folder in your phone's Downloads for easy Cloud syncing
DEST="/sdcard/Download/CANCAN_AUDIT_$(date +%Y%m%d)"
mkdir -p "$DEST"

echo "📂 Syncing to: $DEST"

# 2. Rename and Move Photos + JSONs
count=1
for img in *.jpg; do
    if [ -f "$img" ]; then
        new_name="1501-Pearl-Audit-$(date +%Y%m%d)-$count"
        
        # Copy photo to the cloud-sync folder
        cp "$img" "$DEST/$new_name.jpg"
        
        # Check for a matching JSON (last_audit.json or similar) and copy it
        if [ -f "last_audit.json" ]; then
            cp "last_audit.json" "$DEST/$new_name.json"
        fi
        
        echo "✅ Paired: $new_name"
        ((count++))
    fi
done

echo "🚀 READY FOR DRIVE: Open your Google Drive app and upload the folder from 'Downloads'."
