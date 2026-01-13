#!/bin/bash
# JOHNNY 5 - SELF-HEALING MASTER STRIKE
echo "⚡️ INITIALIZING AUTO-REPAIR STRIKE..."

# 0. PRE-FLIGHT: Clear git locks
rm -f .git/index.lock

# 1. FETCH
LATEST_JSON=$(curl -s -X GET "$SUPABASE_URL/rest/v1/debris_logs?select=objects&order=timestamp.desc&limit=1" \
  -H "apikey: $SUPABASE_KEY" \
  -H "Authorization: Bearer $SUPABASE_KEY")

MATERIAL=$(echo $LATEST_JSON | jq -r '.[0].objects' | jq -r '.[0].material')
FORECAST=$(python3 forecaster.py "$MATERIAL")

# 2. INJECT
sed -i "s|<div id=\"live-feed\">.*|<div id=\"live-feed\"><span class=\"label\">$MATERIAL DETECTED</span>$FORECAST</div>|g" index.html

# 3. DEPLOY
git add .
git commit -m "Johnny 5: Self-Healing Sync - $MATERIAL"
git push origin main
echo "🚀 RECOVERY COMPLETE. WEB UPDATED."
