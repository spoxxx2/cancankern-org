#!/bin/bash
URL="https://cancankern-org.vercel.app"
STATUS=$(curl -o /dev/null -s -w "%{http_code}" $URL)
if [ "$STATUS" == "200" ]; then
  echo "✅ ZENITH ONLINE: $URL is serving Kern County."
else
  echo "⚠️ ZENITH DOWN: Status $STATUS. Check Vercel logs!"
fi
