#!/bin/bash
export PGPASSWORD='37YYNDOhnXwFgTFl'
# Direct column mapping for 100-year forecast
psql -h db.dzrnwzvizztfmjgvpajd.supabase.co -p 5432 -d postgres -U postgres -q -c "INSERT INTO debris_logs (event_id, spectral_calibration, objects) SELECT j->>'event_id', j->'spectral_calibration', j->'objects' FROM (SELECT '$1'::jsonb AS j) AS t;" > /dev/null 2>&1
