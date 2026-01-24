#!/bin/bash
# Zenith Batch Processor - 1501 Pearl St Node

echo "🚀 Starting Daily Batch Audit: $(date)"

# 1. Re-bake the Platinum Website via C++
./zenith_baker

# 2. Find all photos from the last 24 hours (Adjust path if needed)
# This looks in your standard Termux/DCIM storage
PHOTOS=$(find ~/storage/dcim/Camera -name "*.jpg" -mtime -1)

for img in $PHOTOS; do
    echo "Processing: $img"
    # Runs your C++/Python audit engine on the specific image
    # Injects: IP Protection, 100-Year Forecast, and Federal IDs
    python3 twin_gen.py "$img" >> daily_manifest.json
    
    # Sync to Supabase via your PSQL tunnel
    # (Using the JSONB column for high-speed indexing)
    ./sync_cloud.sh "$img"
done

# 3. Final Global Sync
git-zenith
echo "✅ Daily Batch Complete. Platinum Portal Updated."
