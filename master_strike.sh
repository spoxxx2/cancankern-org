#!/bin/bash
# JOHNNY 5 - FORCE OVERRIDE
echo "⚡️ INITIATING FORCE INJECTION..."

# 0. PRE-FLIGHT
rm -f .git/index.lock

# 1. FETCH FROM SUPABASE
LATEST_JSON=$(curl -s -X GET "$SUPABASE_URL/rest/v1/debris_logs?select=objects&order=timestamp.desc&limit=1" \
  -H "apikey: $SUPABASE_KEY" \
  -H "Authorization: Bearer $SUPABASE_KEY")

MATERIAL=$(echo $LATEST_JSON | jq -r '.[0].objects' | jq -r '.[0].material')
FORECAST=$(python3 forecaster.py "$MATERIAL")

# 2. SURGICAL REPLACEMENT
# This targets the entire 'live-feed' div and replaces it entirely
sed -i "s|<div id=\"live-feed\">.*|<div id=\"live-feed\"><span class=\"label\">$MATERIAL DETECTED</span> $FORECAST</div>|g" index.html

# 3. VERIFY LOCAL CHANGE
grep "live-feed" index.html

# 4. PUSH TO LIVE WEB
git add index.html
git commit -m "Johnny 5: Force Update - $MATERIAL"
git push origin main --force
echo "🚀 STRIKE COMPLETE. REFRESH NOW."
