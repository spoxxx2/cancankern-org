#!/bin/bash
# Zenith Deep Archive Audit - 1501 Pearl St Node
# Coverage: Dec 1, 2025 to Present

# 1. Create a local reference file for Dec 1st
START_DATE="202512010000"
touch -t $START_DATE ./start_marker

echo "🕵️ Starting Deep Archive Audit (Since Dec 1st)..."

# 2. Find all photos newer than our marker
# We search common Termux/Android paths
PHOTOS=$(find ~/storage/dcim/Camera /sdcard/DCIM/Camera -name "*.jpg" -newer ./start_marker 2>/dev/null)

COUNT=0
for img in $PHOTOS; do
    echo "Processing Archive Item: $img"
    # Generate Digital Twin + 10-Decade Forecast
    python3 twin_gen.py "$img" >> archive_manifest.json
    
    # Sync to Supabase JSONB
    ./sync_cloud.sh "$img"
    
    COUNT=$((COUNT+1))
done

# 3. Final Re-bake and Sync
./zenith_baker

# Manually running the git commands since aliases don't work in scripts
aud-now
git add .
git commit -m "ZENITH ARCHIVE: $COUNT Items Back-filled (Since Dec 1st)"
git push origin main --force

echo "✅ Archive Complete. $COUNT items added to the Zenith Matrix."
