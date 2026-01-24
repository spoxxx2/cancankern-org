#!/bin/bash
# 1. Update GitHub with latest Audit Log
git add cancan_audit.db ZENITH_MANIFEST.json
git commit -m "ZENITH MATRIX UPDATE: $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main

# 2. Update Website (Triggering a build on cancankern.org)
curl -X POST https://api.vercel.com/v1/integrations/deploy/YOUR_PROJECT_HOOK
echo "🚀 Zenith Matrix: GitHub and Website Synced."
