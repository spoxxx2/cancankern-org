import os, requests

# Get keys from your environment
OC_KEY = os.getenv("OPENCAGE_KEY")
AZ_KEY = os.getenv("AZURE_MAPS_KEY")
LAT, LON = 35.3789, -118.9996  # 1501 Pearl St

print("🧪 --- CANCAN KEY DIAGNOSTIC --- 🧪")

# 1. TEST OPENCAGE
if OC_KEY and "YOUR" not in OC_KEY:
    print(f"📡 Testing OpenCage (Key: {OC_KEY[:4]}...)")
    url = f"https://api.opencagedata.com/geocode/v1/json?q={LAT}+{LON}&key={OC_KEY}"
    r = requests.get(url).json()
    if 'results' in r and len(r['results']) > 0:
        print(f"✅ OPENCAGE SUCCESS: {r['results'][0]['formatted']}")
    else:
        print(f"❌ OPENCAGE FAILED: {r.get('status', {}).get('message', 'Unknown Error')}")
else:
    print("⚠️ OPENCAGE_KEY is missing or a placeholder.")

# 2. TEST AZURE MAPS
if AZ_KEY and "YOUR" not in AZ_KEY:
    print(f"📡 Testing Azure Maps (Key: {AZ_KEY[:4]}...)")
    url = f"https://atlas.microsoft.com/search/address/reverse/json?api-version=1.0&query={LAT},{LON}&subscription-key={AZ_KEY}"
    r = requests.get(url).json()
    if 'addresses' in r:
        print(f"✅ AZURE SUCCESS: {r['addresses'][0]['address']['freeformAddress']}")
    else:
        print(f"❌ AZURE FAILED: {r.get('error', {}).get('message', 'Unknown Error')}")
else:
    print("⚠️ AZURE_MAPS_KEY is missing or a placeholder.")

print("-----------------------------------")
