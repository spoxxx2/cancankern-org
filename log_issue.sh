#!/bin/bash
# CANCAN CleanPath: Terminal Logger

echo "--- CleanPath Kern: Field Entry ---"
read -p "Issue Type (1: Sidewalk, 2: Curb, 3: Road): " ITYPE
read -p "Severity (1-5): " ISEV
read -p "Description: " IDESC

# Mapping types
case $ITYPE in
  1) TYPE="Sidewalk" ;;
  2) TYPE="Curb" ;;
  3) TYPE="Road" ;;
  *) TYPE="General" ;;
esac

# Capture GPS (Requires Termux:API)
LOC=$(termux-location)
LAT=$(echo $LOC | jq .latitude)
LNG=$(echo $LOC | jq .longitude)

# Log to Supabase via our Node Bridge
node -e "
const db = require('./db.js');
db.none('INSERT INTO cleanup_reports(location_lat, location_lng, issue_type, severity, description) VALUES(\$1, \$2, \$3, \$4, \$5)', 
[$LAT, $LNG, '$TYPE', $ISEV, '$IDESC'])
.then(() => {
    console.log('✅ SUCCESS: Incident Logged to Supabase');
    process.exit(0);
})
.catch(err => {
    console.error('❌ ERROR:', err);
    process.exit(1);
});"
