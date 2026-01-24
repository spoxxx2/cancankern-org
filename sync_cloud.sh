#!/bin/bash
# Hardwired Cloud Sync Tunnel
export PGPASSWORD='37YYNDOhnXwFgTFl'
psql -h db.dzrnwzvizztfmjgvpajd.supabase.co -p 5432 -d postgres -U postgres -c "INSERT INTO debris_logs (event_id, spectral_calibration, objects) SELECT j->>'event_id', j->'spectral_calibration', j->'objects' FROM (SELECT '$1'::jsonb AS j) AS t;"
